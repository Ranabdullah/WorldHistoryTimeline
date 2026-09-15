/**
 * Main Application Module
 * Connects Vertical Multi-Track Timeline, Box Zooming, Density Controls,
 * Google Photos Date Scrubber, and In-Window Story Reader.
 */

class WorldTimelineApp {
  constructor() {
    this.renderer = new TimelineRenderer('mainAppContainer');
    this.currentStory = null;
    this.speechSynth = window.speechSynthesis || null;
    this.currentUtterance = null;
    this.isPlayingAudio = false;
    this.readerFontSize = 16;
    
    this.init();
  }

  init() {
    this.buildRegionChips();
    this.attachEventListeners();
    this.updateStoryCountBadge();
    this.renderer.render();
  }

  updateStoryCountBadge() {
    const badge = document.getElementById('storyCountBadge');
    if (badge && typeof STORIES_DATA !== 'undefined') {
      badge.textContent = `${STORIES_DATA.length} Epics & Stories`;
    }
  }

  buildRegionChips() {
    const chipsContainer = document.getElementById('regionChipsBar');
    if (!chipsContainer) return;

    chipsContainer.innerHTML = '';
    REGIONS.forEach(region => {
      const chip = document.createElement('div');
      chip.className = `region-chip ${region.id === 'all' ? 'active' : ''}`;
      chip.dataset.regionId = region.id;
      
      chip.innerHTML = `
        <span class="chip-dot" style="background: ${region.color};"></span>
        <span>${region.icon} ${region.name}</span>
      `;

      chip.addEventListener('click', () => {
        document.querySelectorAll('.region-chip').forEach(c => c.classList.remove('active'));
        chip.classList.add('active');
        this.renderer.setFilters(region.id, this.renderer.searchQuery);
      });

      chipsContainer.appendChild(chip);
    });
  }

  attachEventListeners() {
    // 1. Search Input
    const searchInput = document.getElementById('searchInput');
    if (searchInput) {
      searchInput.addEventListener('input', (e) => {
        this.renderer.setFilters(this.renderer.selectedRegion, e.target.value);
      });
    }

    // 2. Box Zoom Slider (Scale the boxes/cards)
    const boxZoomSlider = document.getElementById('boxZoomSlider');
    if (boxZoomSlider) {
      boxZoomSlider.addEventListener('input', (e) => {
        const val = parseFloat(e.target.value);
        this.renderer.setCardScale(val);
      });
    }

    // 3. Density Mode Toggles (Compact, Regular, Detailed)
    document.querySelectorAll('.density-btn').forEach(btn => {
      btn.addEventListener('click', () => {
        document.querySelectorAll('.density-btn').forEach(b => b.classList.remove('active'));
        btn.classList.add('active');
        const mode = btn.dataset.density;
        this.renderer.setDensity(mode);
        this.renderer.render();
      });
    });

    // 4. Reset Button
    const resetBtn = document.getElementById('resetBtn');
    if (resetBtn) {
      resetBtn.addEventListener('click', () => {
        if (boxZoomSlider) boxZoomSlider.value = 1.0;
        this.renderer.setCardScale(1.0);
        this.renderer.setDensity('regular');
        document.querySelectorAll('.density-btn').forEach(b => b.classList.toggle('active', b.dataset.density === 'regular'));
        this.renderer.setFilters('all', '');
        if (searchInput) searchInput.value = '';
        document.querySelectorAll('.region-chip').forEach(c => c.classList.toggle('active', c.dataset.regionId === 'all'));
        const container = document.getElementById('mainAppContainer');
        if (container) container.scrollTo({ top: 0, left: 0, behavior: 'smooth' });
      });
    }

    // 5. In-Window Reader Modal Controls
    const readerOverlay = document.getElementById('readerOverlay');
    const readerCloseBtn = document.getElementById('readerCloseBtn');
    if (readerOverlay) readerOverlay.addEventListener('click', () => this.closeReader());
    if (readerCloseBtn) readerCloseBtn.addEventListener('click', () => this.closeReader());

    document.addEventListener('keydown', (e) => {
      if (e.key === 'Escape') {
        this.closeReader();
        this.closeModal('aboutModal');
      }
    });

    // 6. Audio Speech Narration
    const playAudioBtn = document.getElementById('btnPlayAudio');
    if (playAudioBtn) {
      playAudioBtn.addEventListener('click', () => this.toggleSpeechNarration());
    }

    // 7. Reader Font Resizer
    const fontPlusBtn = document.getElementById('btnFontPlus');
    const fontMinusBtn = document.getElementById('btnFontMinus');
    if (fontPlusBtn) {
      fontPlusBtn.addEventListener('click', () => {
        this.readerFontSize = Math.min(24, this.readerFontSize + 2);
        this.applyReaderFontSize();
      });
    }
    if (fontMinusBtn) {
      fontMinusBtn.addEventListener('click', () => {
        this.readerFontSize = Math.max(12, this.readerFontSize - 2);
        this.applyReaderFontSize();
      });
    }

    // 8. About Modal
    const aboutBtn = document.getElementById('aboutBtn');
    const aboutCloseBtn = document.getElementById('aboutCloseBtn');
    if (aboutBtn) aboutBtn.addEventListener('click', () => this.openModal('aboutModal'));
    if (aboutCloseBtn) aboutCloseBtn.addEventListener('click', () => this.closeModal('aboutModal'));

    // 9. Live Web Story Harvester Modal
    const harvestWebBtn = document.getElementById('harvestWebBtn');
    const harvestCloseBtn = document.getElementById('harvestCloseBtn');
    const btnExecuteHarvest = document.getElementById('btnExecuteHarvest');
    const harvestInput = document.getElementById('harvestInput');
    const btnAddHarvestedStory = document.getElementById('btnAddHarvestedStory');

    if (harvestWebBtn) harvestWebBtn.addEventListener('click', () => this.openModal('harvestModal'));
    if (harvestCloseBtn) harvestCloseBtn.addEventListener('click', () => this.closeModal('harvestModal'));

    if (btnExecuteHarvest && harvestInput) {
      btnExecuteHarvest.addEventListener('click', () => this.executeLiveWebHarvest());
      harvestInput.addEventListener('keydown', (e) => {
        if (e.key === 'Enter') this.executeLiveWebHarvest();
      });
    }

    if (btnAddHarvestedStory) {
      btnAddHarvestedStory.addEventListener('click', () => this.addHarvestedStoryToTimeline());
    }
  }

  async executeLiveWebHarvest() {
    const input = document.getElementById('harvestInput');
    const status = document.getElementById('harvestStatus');
    const preview = document.getElementById('harvestPreview');
    if (!input || !input.value.trim()) return;

    const query = input.value.trim();
    status.style.color = 'var(--text-main)';
    status.textContent = `🔍 Searching internet for "${query}"...`;
    preview.style.display = 'none';

    try {
      const encoded = encodeURIComponent(query.replace(/ /g, '_'));
      const res = await fetch(`https://en.wikipedia.org/api/rest_v1/page/summary/${encoded}`);
      if (!res.ok) {
        throw new Error('Not found on Wikipedia');
      }
      const data = await res.json();
      
      const regionId = this.detectRegionFromText(`${data.title} ${data.description || ''} ${data.extract || ''}`);
      const year = this.detectYearFromText(`${data.title} ${data.description || ''} ${data.extract || ''}`);
      const era = year < -3000 ? 'prehistory' : (year < -1200 ? 'bronze' : (year < 500 ? 'classical' : (year < 1400 ? 'medieval' : 'renaissance')));
      const displayDate = year < 0 ? `c. ${Math.abs(year).toLocaleString()} BCE` : `c. ${year} CE`;

      const regionMeta = REGIONS.find(r => r.id === regionId) || { name: 'World Classics', icon: '✒️' };

      this.pendingHarvestedStory = {
        id: `harvest-${Date.now()}-${data.title.toLowerCase().replace(/[^a-z0-9]+/g, '-')}`,
        year: year,
        displayDate: displayDate,
        era: era,
        regionId: regionId,
        regionName: regionMeta.name,
        place: data.description || `${regionMeta.name} Region`,
        author: `Classical ${regionMeta.name} Lore`,
        title: data.title,
        subtitle: data.description || `The Chronicle of ${data.title}`,
        summary: data.extract || 'A timeless world epic.',
        fullStory: `### Act I: The Tale of ${data.title}\n${data.extract}\n\n### Act II: The Great Deeds\nPassed across centuries as an enduring narrative of human imagination.\n\n### Act III: Immortality in Literature\nPreserved in world heritage manuscripts and folklore.`,
        characters: [{ name: data.title, role: 'Protagonist', desc: data.description || 'Central mythic figure.' }],
        themes: ['World Heritage', 'Mythology', 'Heroic Legacy'],
        echoes: 'Shares foundational motifs across world storytelling.',
        famousQuote: `“The legacy of ${data.title} endures throughout the ages.”`,
        historicalContext: 'Harvested directly from open encyclopedia archives.'
      };

      document.getElementById('harvestPreviewDate').textContent = `${regionMeta.icon} ${regionMeta.name} · ${displayDate}`;
      document.getElementById('harvestPreviewTitle').textContent = data.title;
      document.getElementById('harvestPreviewExtract').textContent = data.extract;
      
      status.style.color = '#15803d';
      status.textContent = `✅ Story found on the web!`;
      preview.style.display = 'block';

    } catch (err) {
      status.style.color = '#b91c1c';
      status.textContent = `❌ Could not find story for "${query}". Try another title (e.g. "Perseus", "Tristan and Iseult", "Moby-Dick").`;
    }
  }

  addHarvestedStoryToTimeline() {
    if (!this.pendingHarvestedStory) return;

    STORIES_DATA.push(this.pendingHarvestedStory);
    STORIES_DATA.sort((a, b) => a.year - b.year);

    this.updateStoryCountBadge();
    this.renderer.render();
    this.closeModal('harvestModal');

    // Scroll to the new story
    const targetY = this.renderer.yearToY(this.pendingHarvestedStory.year);
    const container = document.getElementById('mainAppContainer');
    if (container) {
      container.scrollTo({ top: Math.max(0, targetY - 120), behavior: 'smooth' });
    }

    // Open Reader for the new story immediately
    this.openReader(this.pendingHarvestedStory);
    this.pendingHarvestedStory = null;
  }

  detectRegionFromText(text) {
    const lower = text.toLowerCase();
    if (lower.includes('greece') || lower.includes('greek') || lower.includes('rome') || lower.includes('roman') || lower.includes('athens') || lower.includes('latin')) return 'greece_rome';
    if (lower.includes('mesopotamia') || lower.includes('sumer') || lower.includes('babylon') || lower.includes('akkad') || lower.includes('uruk')) return 'mesopotamia';
    if (lower.includes('egypt') || lower.includes('pharaoh') || lower.includes('nile') || lower.includes('pyramid') || lower.includes('thebes')) return 'egypt';
    if (lower.includes('india') || lower.includes('sanskrit') || lower.includes('vedic') || lower.includes('hindu') || lower.includes('buddha')) return 'india';
    if (lower.includes('china') || lower.includes('chinese') || lower.includes('dynasty') || lower.includes('daoism') || lower.includes('confucius')) return 'china';
    if (lower.includes('persia') || lower.includes('iran') || lower.includes('zoroastrian') || lower.includes('shahnameh') || lower.includes('baghdad')) return 'persia_arabia';
    if (lower.includes('japan') || lower.includes('korea') || lower.includes('shinto') || lower.includes('heian') || lower.includes('joseon')) return 'japan_korea';
    if (lower.includes('maya') || lower.includes('aztec') || lower.includes('inca') || lower.includes('mesoamerica') || lower.includes('lakota') || lower.includes('cherokee')) return 'americas';
    if (lower.includes('mali') || lower.includes('yoruba') || lower.includes('ethiopia') || lower.includes('zulu') || lower.includes('ashanti') || lower.includes('africa')) return 'africa';
    if (lower.includes('norse') || lower.includes('viking') || lower.includes('celtic') || lower.includes('irish') || lower.includes('welsh') || lower.includes('arthur') || lower.includes('beowulf')) return 'n_europe';
    if (lower.includes('aboriginal') || lower.includes('dreamtime') || lower.includes('polynesia') || lower.includes('maori') || lower.includes('hawaii') || lower.includes('maui')) return 'oceania';
    if (lower.includes('israel') || lower.includes('canaan') || lower.includes('bible') || lower.includes('hebrew') || lower.includes('torah')) return 'levant';
    return 'world_classics';
  }

  detectYearFromText(text) {
    const matchBce = text.match(/(\d+)\s*(?:BCE|BC)/i);
    if (matchBce) return -parseInt(matchBce[1]);
    const matchCentBce = text.match(/(\d+)(?:st|nd|rd|th)\s*century\s*(?:BCE|BC)/i);
    if (matchCentBce) return -(parseInt(matchCentBce[1]) * 100 - 50);
    const matchCentCe = text.match(/(\d+)(?:st|nd|rd|th)\s*century\s*(?:CE|AD)?/i);
    if (matchCentCe) return parseInt(matchCentCe[1]) * 100 - 50;
    const matchYr = text.match(/\b(1[0-8]\d{2}|[5-9]\d{2})\b/);
    if (matchYr) return parseInt(matchYr[1]);
    return 800;
  }

  /* ==========================================================================
     IN-WINDOW STORY READER
     ========================================================================== */
  openReader(story) {
    this.currentStory = story;
    this.stopSpeech();

    const overlay = document.getElementById('readerOverlay');
    const windowEl = document.getElementById('readerWindow');
    if (!overlay || !windowEl) return;

    const regionMeta = REGIONS.find(r => r.id === story.regionId) || { icon: '📜', color: '#111' };

    document.getElementById('readerBreadcrumbs').innerHTML = `
      <span>${regionMeta.icon} ${story.regionName}</span>
      <span>•</span>
      <span>${story.place || 'World Heritage'}</span>
    `;

    document.getElementById('readerDatePill').textContent = story.displayDate;
    document.getElementById('readerTitle').textContent = story.title;
    document.getElementById('readerSubtitle').textContent = story.subtitle || '';

    document.getElementById('readerAuthorDetails').innerHTML = `
      <h4>✍️ ${story.author}</h4>
      <p>Setting: ${story.place || 'Ancient World'} · Date: ${story.displayDate}</p>
    `;

    const acts = this.parseStoryActs(story.fullStory || story.summary);
    this.renderActTabs(acts);
    this.renderStoryContent(story.fullStory || story.summary);

    const quoteContainer = document.getElementById('readerQuoteContainer');
    if (story.famousQuote) {
      quoteContainer.style.display = 'block';
      quoteContainer.innerHTML = `<p>${story.famousQuote}</p>`;
    } else {
      quoteContainer.style.display = 'none';
    }

    const charsContainer = document.getElementById('readerCharactersGrid');
    const charsSection = document.getElementById('readerCharactersSection');
    if (story.characters && story.characters.length > 0) {
      charsSection.style.display = 'block';
      charsContainer.innerHTML = '';
      story.characters.forEach(char => {
        const charCard = document.createElement('div');
        charCard.className = 'character-card';
        charCard.innerHTML = `
          <h5>${char.name}</h5>
          <div class="char-role">${char.role}</div>
          <p>${char.desc}</p>
        `;
        charsContainer.appendChild(charCard);
      });
    } else {
      charsSection.style.display = 'none';
    }

    const echoesSection = document.getElementById('readerEchoesSection');
    const echoesText = document.getElementById('readerEchoesText');
    if (story.echoes) {
      echoesSection.style.display = 'block';
      echoesText.textContent = story.echoes;
    } else {
      echoesSection.style.display = 'none';
    }

    const historySection = document.getElementById('readerHistorySection');
    const historyText = document.getElementById('readerHistoryText');
    if (story.historicalContext) {
      historySection.style.display = 'block';
      historyText.textContent = story.historicalContext;
    } else {
      historySection.style.display = 'none';
    }

    const themesContainer = document.getElementById('readerThemesList');
    if (story.themes && story.themes.length > 0) {
      themesContainer.innerHTML = story.themes.map(t => `<span class="theme-tag">${t}</span>`).join('');
    } else {
      themesContainer.innerHTML = '';
    }

    this.applyReaderFontSize();

    overlay.classList.add('active');
    windowEl.classList.add('active');

    const readerBody = document.getElementById('readerBody');
    if (readerBody) readerBody.scrollTop = 0;
  }

  closeReader() {
    this.stopSpeech();
    const overlay = document.getElementById('readerOverlay');
    const windowEl = document.getElementById('readerWindow');
    if (overlay) overlay.classList.remove('active');
    if (windowEl) windowEl.classList.remove('active');
    this.currentStory = null;
  }

  parseStoryActs(fullStoryText) {
    const lines = fullStoryText.split('\n');
    const acts = [];
    lines.forEach(line => {
      if (line.startsWith('### ')) {
        acts.push(line.replace('### ', '').trim());
      }
    });
    return acts;
  }

  renderActTabs(acts) {
    const tabsContainer = document.getElementById('readerActTabs');
    if (!tabsContainer) return;

    if (acts.length <= 1) {
      tabsContainer.style.display = 'none';
      return;
    }

    tabsContainer.style.display = 'flex';
    tabsContainer.innerHTML = '';

    acts.forEach((actTitle, idx) => {
      const tabBtn = document.createElement('button');
      tabBtn.className = `act-tab-btn ${idx === 0 ? 'active' : ''}`;
      tabBtn.textContent = actTitle;

      tabBtn.addEventListener('click', () => {
        document.querySelectorAll('.act-tab-btn').forEach(b => b.classList.remove('active'));
        tabBtn.classList.add('active');
        const headings = document.querySelectorAll('#readerStoryContent h3');
        if (headings[idx]) {
          headings[idx].scrollIntoView({ behavior: 'smooth', block: 'start' });
        }
      });

      tabsContainer.appendChild(tabBtn);
    });
  }

  renderStoryContent(rawMarkdown) {
    const container = document.getElementById('readerStoryContent');
    if (!container) return;

    let html = rawMarkdown
      .replace(/^### (.*$)/gim, '<h3 id="act-$1">$1</h3>')
      .replace(/^## (.*$)/gim, '<h2>$1</h2>')
      .replace(/\*\*(.*?)\*\*/gim, '<strong>$1</strong>')
      .replace(/\*(.*?)\*/gim, '<em>$1</em>');

    const paragraphs = html.split('\n\n');
    html = paragraphs.map(p => {
      p = p.trim();
      if (!p) return '';
      if (p.startsWith('<h3') || p.startsWith('<h2')) return p;
      return `<p>${p}</p>`;
    }).join('');

    container.innerHTML = html;
  }

  applyReaderFontSize() {
    const storyContent = document.getElementById('readerStoryContent');
    if (storyContent) {
      storyContent.style.fontSize = `${this.readerFontSize}px`;
    }
  }

  toggleSpeechNarration() {
    if (!this.speechSynth) {
      alert('Speech synthesis is not supported in your browser.');
      return;
    }

    const playBtn = document.getElementById('btnPlayAudio');

    if (this.isPlayingAudio) {
      this.stopSpeech();
      if (playBtn) playBtn.innerHTML = `<span>▶</span> Listen to Story`;
    } else {
      if (!this.currentStory) return;
      
      const cleanText = `${this.currentStory.title}. By ${this.currentStory.author}. ${this.currentStory.summary}. ${this.currentStory.fullStory.replace(/###/g, '').replace(/\*/g, '')}`;
      
      this.currentUtterance = new SpeechSynthesisUtterance(cleanText);
      this.currentUtterance.rate = 0.95;
      this.currentUtterance.pitch = 1.0;

      this.currentUtterance.onend = () => {
        this.isPlayingAudio = false;
        if (playBtn) playBtn.innerHTML = `<span>▶</span> Listen to Story`;
      };

      this.currentUtterance.onerror = () => {
        this.isPlayingAudio = false;
        if (playBtn) playBtn.innerHTML = `<span>▶</span> Listen to Story`;
      };

      this.speechSynth.speak(this.currentUtterance);
      this.isPlayingAudio = true;
      if (playBtn) playBtn.innerHTML = `<span>⏸</span> Pause Narration`;
    }
  }

  stopSpeech() {
    if (this.speechSynth && this.isPlayingAudio) {
      this.speechSynth.cancel();
      this.isPlayingAudio = false;
      const playBtn = document.getElementById('btnPlayAudio');
      if (playBtn) playBtn.innerHTML = `<span>▶</span> Listen to Story`;
    }
  }

  openModal(modalId) {
    const modal = document.getElementById(modalId);
    if (modal) modal.classList.add('active');
  }

  closeModal(modalId) {
    const modal = document.getElementById(modalId);
    if (modal) modal.classList.remove('active');
  }
}

document.addEventListener('DOMContentLoaded', () => {
  window.App = new WorldTimelineApp();
});
