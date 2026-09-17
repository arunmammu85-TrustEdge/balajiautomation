import re

# 1. FIX INDEX.HTML FABs
with open('index.html', 'r') as f:
    html = f.read()

new_fabs = """
<div class="fab-container">
  <button id="fab-top" class="fab fab-top" aria-label="Scroll to top" style="background:var(--text-dim);">
    <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><line x1="12" y1="19" x2="12" y2="5"></line><polyline points="5 12 12 5 19 12"></polyline></svg>
  </button>
  <a href="tel:+919008066215" class="fab fab-call" aria-label="Call" style="background:var(--accent);">
    <svg width="24" height="24" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M22 16.92v3a2 2 0 0 1-2.18 2 19.79 19.79 0 0 1-8.63-3.07 19.5 19.5 0 0 1-6-6 19.79 19.79 0 0 1-3.07-8.67A2 2 0 0 1 4.11 2h3a2 2 0 0 1 2 1.72 12.84 12.84 0 0 0 .7 2.81 2 2 0 0 1-.45 2.11L8.09 9.91a16 16 0 0 0 6 6l1.27-1.27a2 2 0 0 1 2.11-.45 12.84 12.84 0 0 0 2.81.7A2 2 0 0 1 22 16.92z"></path></svg>
  </a>
  <a href="https://wa.me/919008066215" class="fab fab-wa" target="_blank" rel="noopener" aria-label="WhatsApp" style="background:#25D366;">
    <svg width="28" height="28" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2" stroke-linecap="round" stroke-linejoin="round"><path d="M22 16.92v3a2 2 0 0 1-2.18 2 19.79 19.79 0 0 1-8.63-3.07 19.5 19.5 0 0 1-6-6 19.79 19.79 0 0 1-3.07-8.67A2 2 0 0 1 4.11 2h3a2 2 0 0 1 2 1.72 12.84 12.84 0 0 0 .7 2.81 2 2 0 0 1-.45 2.11L8.09 9.91a16 16 0 0 0 6 6l1.27-1.27a2 2 0 0 1 2.11-.45 12.84 12.84 0 0 0 2.81.7A2 2 0 0 1 22 16.92z"></path></svg>
  </a>
</div>
<script src="assets/js/main.js"></script>
"""

# Replace all fab-container sections
html = re.sub(r'<div class="fab-container.*?<script src="assets/js/main.js"></script>', new_fabs, html, flags=re.DOTALL)

with open('index.html', 'w') as f:
    f.write(html)

# 2. FIX CSS for FABs
with open('assets/css/style.css', 'r') as f:
    css = f.read()

# Make sure FABs are circles
css = css.replace('.fab-wa { background: #25D366; width: auto; padding: 0 20px; border-radius: 28px; }', '.fab-wa { background: #25D366; width: 56px; height: 56px; border-radius: 50%; padding: 0; }')
css = css.replace('.fab-call { background: var(--accent); width: auto; padding: 0 20px; border-radius: 28px; }', '.fab-call { background: var(--accent); width: 56px; height: 56px; border-radius: 50%; padding: 0; }')

with open('assets/css/style.css', 'w') as f:
    f.write(css)

# 3. FIX JS Counter Animation
with open('assets/js/main.js', 'r') as f:
    js = f.read()

new_counter_code = """
  // Animated Number Counters using requestAnimationFrame
  const counters = document.querySelectorAll('.num[data-target]');
  const duration = 2000; // 2 seconds

  function animateCounter(counter) {
    const target = +counter.getAttribute('data-target');
    const suffix = counter.getAttribute('data-suffix') || '';
    let startTimestamp = null;
    
    const step = (timestamp) => {
      if (!startTimestamp) startTimestamp = timestamp;
      const progress = Math.min((timestamp - startTimestamp) / duration, 1);
      // easeOutExpo
      const easeProgress = progress === 1 ? 1 : 1 - Math.pow(2, -10 * progress);
      
      const current = Math.floor(easeProgress * target);
      counter.innerText = current + suffix;
      
      if (progress < 1) {
        window.requestAnimationFrame(step);
      } else {
        counter.innerText = target + suffix;
      }
    };
    window.requestAnimationFrame(step);
  }
"""

js = re.sub(r'// Animated Number Counters.*?function resetCounters', new_counter_code + '\n  function resetCounters', js, flags=re.DOTALL)

with open('assets/js/main.js', 'w') as f:
    f.write(js)

print("All fixes applied successfully.")
