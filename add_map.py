with open('index.html', 'r') as f:
    html = f.read()

old_html = """      </div>
    </div>
  </div>
</section>"""

new_html = """      </div>
    </div>
    
    <div style="margin-top: 48px; width: 100%; border-radius: 12px; overflow: hidden; box-shadow: 0 4px 16px rgba(0,0,0,0.05);">
      <iframe src="https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d4873.876749845079!2d77.51497397592472!3d13.03855761340508!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x3bae3d1e04e089ad%3A0xe3649dd53ab32592!2sBALAJI%20AUTOMATION!5e1!3m2!1sen!2sin!4v1789663054946!5m2!1sen!2sin" width="100%" height="450" style="border:0; display:block;" allowfullscreen="" loading="lazy" referrerpolicy="strict-origin-when-cross-origin"></iframe>
    </div>
  </div>
</section>"""

html = html.replace(old_html, new_html)

with open('index.html', 'w') as f:
    f.write(html)

print("Map added to contact section.")
