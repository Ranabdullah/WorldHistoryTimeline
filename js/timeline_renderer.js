/**
 * Vertical Multi-Track Timeline Renderer
 * Ultra-compact rendering: fits all 13 world tracks simultaneously on 1920x1080 screens
 * and provides responsive layout on phones and mobile viewports.
 */

class TimelineRenderer {
  constructor(containerId) {
    this.container = document.getElementById(containerId);
    this.cardScale = 1.0;
    this.density = 'regular'; // 'compact' | 'regular' | 'detailed'
    this.selectedRegion = 'all';
    this.searchQuery = '';
    
    // Calibrated Vertical Segment Scale (from 10,000 BCE to 1800 CE)
    this.segments = [
      { start: -10000, end: -3000, height: 1600 },
      { start: -3000,  end: -1000, height: 2000 },
      { start: -1000,  end: 0,     height: 2000 },
      { start: 0,      end: 1000,  height: 1800 },
      { start: 1000,   end: 1800,  height: 2200 }
    ];

    this.axisTicks = [
      -10000, -8000, -6000, -5000, -4000, -3000, -2500, -2000, -1750, 
      -1500, -1200, -1000, -800, -600, -400, -200, 0, 200, 400, 
      600, 800, 1000, 1150, 1300, 1400, 1500, 1600, 1700, 1800
    ];

    this.totalHeight = this.segments.reduce((sum, seg) => sum + seg.height, 0);
  }

  yearToY(year) {
    let y = 45;
    for (const seg of this.segments) {
      if (year >= seg.end) {
        y += seg.height;
        continue;
      }
      if (year <= seg.start) {
        return y;
      }
      const ratio = (year - seg.start) / (seg.end - seg.start);
      y += ratio * seg.height;
      return y;
    }
    return y;
  }

  yToYear(y) {
    let currY = 45;
    if (y <= currY) return -10000;
    for (const seg of this.segments) {
      if (y <= currY + seg.height) {
        const ratio = (y - currY) / seg.height;
        return Math.round(seg.start + ratio * (seg.end - seg.start));
      }
      currY += seg.height;
    }
    return 1800;
  }

  formatYear(year) {
    if (year < 0) return `${Math.abs(year).toLocaleString()} BCE`;
    if (year === 0) return '1 BCE/CE';
    return `${year.toLocaleString()} CE`;
  }

  setCardScale(scale) {
    this.cardScale = Math.min(2.5, Math.max(0.5, scale));
    const baseTrack = window.innerWidth <= 768 ? 150 : 136;
    const baseCard = window.innerWidth <= 768 ? 130 : 120;

    document.documentElement.style.setProperty('--card-scale', this.cardScale);
    document.documentElement.style.setProperty('--card-width', `${baseCard * this.cardScale}px`);
    document.documentElement.style.setProperty('--track-width', `${baseTrack * this.cardScale}px`);
  }

  setDensity(densityMode) {
    this.density = densityMode;
    if (this.container) {
      this.container.classList.remove('density-compact', 'density-regular', 'density-detailed');
      this.container.classList.add(`density-${densityMode}`);
    }
  }

  setFilters(region, search) {
    this.selectedRegion = region;
    this.searchQuery = search ? search.toLowerCase().trim() : '';
    this.render();
  }

  getFilteredStories() {
    return STORIES_DATA.filter(story => {
      if (this.selectedRegion !== 'all' && story.regionId !== this.selectedRegion) {
        return false;
      }
      if (this.searchQuery) {
        const fullText = (
          story.title + ' ' + 
          story.subtitle + ' ' + 
          story.author + ' ' + 
          story.place + ' ' + 
          story.regionName + ' ' + 
          story.summary + ' ' +
          (story.themes ? story.themes.join(' ') : '') + ' ' +
          (story.characters ? story.characters.map(c => c.name).join(' ') : '')
        ).toLowerCase();
        
        if (!fullText.includes(this.searchQuery)) {
          return false;
        }
      }
      return true;
    });
  }

  render() {
    const filteredStories = this.getFilteredStories();
    const activeRegions = this.selectedRegion === 'all' 
      ? REGIONS.filter(r => r.id !== 'all')
      : REGIONS.filter(r => r.id === this.selectedRegion);

    this.container.innerHTML = '';

    const boardWrapper = document.createElement('div');
    boardWrapper.className = 'vertical-board-wrapper';
    boardWrapper.style.height = (this.totalHeight + 350) + 'px';

    // ==========================================
    // 1. LEFT STICKY TIME AXIS COLUMN
    // ==========================================
    const timeAxisCol = document.createElement('div');
    timeAxisCol.className = 'time-axis-column';
    timeAxisCol.style.height = (this.totalHeight + 350) + 'px';

    const axisHeader = document.createElement('div');
    axisHeader.className = 'time-axis-header';
    axisHeader.textContent = 'Date';
    timeAxisCol.appendChild(axisHeader);

    const ticksContainer = document.createElement('div');
    ticksContainer.className = 'time-axis-ticks-container';
    ticksContainer.style.height = (this.totalHeight + 300) + 'px';

    this.axisTicks.forEach(year => {
      const y = this.yearToY(year);
      const tick = document.createElement('div');
      tick.className = 'time-axis-tick';
      tick.style.top = y + 'px';
      tick.textContent = this.formatYear(year);
      ticksContainer.appendChild(tick);
    });

    timeAxisCol.appendChild(ticksContainer);
    boardWrapper.appendChild(timeAxisCol);

    // ==========================================
    // 2. REGIONAL TRACKS WITH DOTTED LINES
    // ==========================================
    const tracksContainer = document.createElement('div');
    tracksContainer.className = 'tracks-container';

    activeRegions.forEach(region => {
      const trackCol = document.createElement('div');
      trackCol.className = 'region-track-column';
      trackCol.dataset.regionId = region.id;
      trackCol.style.height = (this.totalHeight + 350) + 'px';

      // Track Header (Sticky Top)
      const trackHeader = document.createElement('div');
      trackHeader.className = 'region-track-header';
      trackHeader.title = region.name;
      trackHeader.innerHTML = `
        <span class="track-badge-dot" style="background: ${region.color};"></span>
        <span>${region.icon} ${region.name}</span>
      `;
      trackCol.appendChild(trackHeader);

      // Find stories belonging to this region
      const regionStories = filteredStories.filter(s => s.regionId === region.id);
      
      let lastPlacedY = -999;

      regionStories.forEach(story => {
        let y = this.yearToY(story.year);
        const minSpacing = this.density === 'compact' ? 52 : (this.density === 'detailed' ? 160 : 96);
        if (y < lastPlacedY + minSpacing) {
          y = lastPlacedY + minSpacing;
        }
        lastPlacedY = y;

        // Card Element
        const cardEl = document.createElement('div');
        cardEl.className = 'story-card-v';
        cardEl.style.top = y + 'px';
        cardEl.dataset.storyId = story.id;
        cardEl.title = `${story.title} (${story.displayDate})`;

        cardEl.innerHTML = `
          <div class="track-node-dot" style="border-color: ${region.color};"></div>
          <div class="card-content-box">
            <span class="card-date-badge">${story.displayDate.split('(')[0].trim()}</span>
            <h4 class="card-title-text">${story.title}</h4>
            <div class="card-author-text">✍️ ${story.author}</div>
            <p class="card-summary-snippet">${story.summary}</p>
            <div class="card-footer-prompt">
              <span>Read →</span>
            </div>
          </div>
        `;

        cardEl.addEventListener('click', () => {
          if (window.App) window.App.openReader(story);
        });

        trackCol.appendChild(cardEl);
      });

      tracksContainer.appendChild(trackCol);
    });

    boardWrapper.appendChild(tracksContainer);
    this.container.appendChild(boardWrapper);

    this.setupDateScrubber();
    this.attachPanNavigation();
  }

  /* ==========================================================================
     3. GOOGLE PHOTOS STYLE DATE SCRUBBER (RIGHT SIDE RAIL)
     ========================================================================== */
  setupDateScrubber() {
    let scrubber = document.getElementById('dateScrubberPanel');
    if (!scrubber) {
      scrubber = document.createElement('div');
      scrubber.id = 'dateScrubberPanel';
      scrubber.className = 'date-scrubber-panel';
      document.body.appendChild(scrubber);
    }

    scrubber.innerHTML = '<div class="scrubber-axis-line"></div>';

    const scrubberDates = (typeof SCRUBBER_DATES !== 'undefined') ? SCRUBBER_DATES : [
      { year: -10000, label: '10k BCE' },
      { year: -5000,  label: '5k BCE' },
      { year: -3000,  label: '3k BCE' },
      { year: -1200,  label: '1.2k BCE' },
      { year: 0,      label: '1 CE' },
      { year: 1000,   label: '1k CE' },
      { year: 1400,   label: '1.4k CE' },
      { year: 1800,   label: '1.8k CE' }
    ];

    scrubberDates.forEach(d => {
      const node = document.createElement('div');
      node.className = 'scrubber-date-node';
      node.innerHTML = `<span class="scrubber-date-label">${d.label}</span>`;
      
      node.addEventListener('click', () => {
        const targetY = this.yearToY(d.year);
        this.container.scrollTo({ top: Math.max(0, targetY - 100), behavior: 'smooth' });
      });

      scrubber.appendChild(node);
    });

    let tooltip = document.getElementById('floatingYearTooltip');
    if (!tooltip) {
      tooltip = document.createElement('div');
      tooltip.id = 'floatingYearTooltip';
      tooltip.className = 'floating-year-tooltip';
      document.body.appendChild(tooltip);
    }

    this.container.addEventListener('scroll', () => {
      const scrollTop = this.container.scrollTop;
      const currentYear = this.yToYear(scrollTop + 120);
      tooltip.textContent = this.formatYear(currentYear);
      
      const scrollRatio = scrollTop / (this.totalHeight || 1);
      const scrubberHeight = scrubber.clientHeight - 30;
      tooltip.style.top = `${scrubber.offsetTop + 15 + scrollRatio * scrubberHeight}px`;
      tooltip.classList.add('visible');

      clearTimeout(this.tooltipTimeout);
      this.tooltipTimeout = setTimeout(() => {
        tooltip.classList.remove('visible');
      }, 1000);
    });
  }

  /* ==========================================================================
     4. MIDDLE-MOUSE & PAN NAVIGATION
     ========================================================================== */
  attachPanNavigation() {
    let isPanning = false;
    let startX = 0, startY = 0;
    let startScrollLeft = 0, startScrollTop = 0;

    const onMouseDown = (e) => {
      if (e.button === 1 || (!e.target.closest('.story-card-v') && !e.target.closest('.date-scrubber-panel'))) {
        isPanning = true;
        this.container.classList.add('panning');
        startX = e.clientX;
        startY = e.clientY;
        startScrollLeft = this.container.scrollLeft;
        startScrollTop = this.container.scrollTop;
        e.preventDefault();
      }
    };

    const onMouseMove = (e) => {
      if (!isPanning) return;
      const dx = e.clientX - startX;
      const dy = e.clientY - startY;
      this.container.scrollLeft = startScrollLeft - dx;
      this.container.scrollTop = startScrollTop - dy;
    };

    const onMouseUp = () => {
      if (isPanning) {
        isPanning = false;
        this.container.classList.remove('panning');
      }
    };

    this.container.addEventListener('mousedown', onMouseDown);
    window.addEventListener('mousemove', onMouseMove);
    window.addEventListener('mouseup', onMouseUp);
  }
}

window.TimelineRenderer = TimelineRenderer;
