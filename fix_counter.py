import re

with open('assets/js/main.js', 'r') as f:
    js = f.read()

new_counter_code = """
  // Animated Number Counters using requestAnimationFrame
  const counters = document.querySelectorAll('.num[data-target]');
  const duration = 2000; // 2 seconds

  function animateCounter(counter) {
    if (counter.dataset.animId) {
      cancelAnimationFrame(parseInt(counter.dataset.animId));
    }
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
        counter.dataset.animId = window.requestAnimationFrame(step);
      }
    };
    counter.dataset.animId = window.requestAnimationFrame(step);
  }

  const counterObserver = new IntersectionObserver((entries) => {
    entries.forEach(entry => {
      const counter = entry.target;
      if (entry.isIntersecting) {
        animateCounter(counter);
      } else {
        // Reset when out of view so it runs again
        if (counter.dataset.animId) cancelAnimationFrame(parseInt(counter.dataset.animId));
        counter.innerText = '0' + (counter.getAttribute('data-suffix') || '');
      }
    });
  }, { threshold: 0.1 });

  counters.forEach(counter => {
    counterObserver.observe(counter);
  });
"""

# Replace old counter logic completely
# We know the old logic starts at "// Animated Number Counters" and ends just before "});" at the end of the file
# We will use regex to replace it
js = re.sub(r'// Animated Number Counters.*?counters\.forEach\(counter => \{\s*observer\.observe\(counter\);\s*\}\);', new_counter_code, js, flags=re.DOTALL)

with open('assets/js/main.js', 'w') as f:
    f.write(js)

print("Counter loop fixed.")
