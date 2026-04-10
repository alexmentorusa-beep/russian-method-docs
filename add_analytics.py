import os
import glob

GA_SCRIPT = """<!-- Google tag (gtag.js) -->
<script async src="https://www.googletagmanager.com/gtag/js?id=G-T1GD43HJLV"></script>
<script>
  window.dataLayer = window.dataLayer || [];
  function gtag(){dataLayer.push(arguments);}
  gtag('js', new Date());
  gtag('config', 'G-T1GD43HJLV');
</script>"""

# Get all HTML files in current directory
html_files = glob.glob("*.html")

if not html_files:
    print("❌ No HTML files found. Make sure you run this script in your russian-method-docs folder.")
else:
    updated = 0
    skipped = 0

    for filename in html_files:
        with open(filename, "r", encoding="utf-8") as f:
            content = f.read()

        if "G-T1GD43HJLV" in content:
            print(f"⏭️  {filename} — already has Analytics, skipped")
            skipped += 1
        elif "<head>" in content:
            content = content.replace("<head>", "<head>\n" + GA_SCRIPT, 1)
            with open(filename, "w", encoding="utf-8") as f:
                f.write(content)
            print(f"✅ {filename} — updated")
            updated += 1
        else:
            print(f"⚠️  {filename} — no <head> tag found, skipped")
            skipped += 1

    print(f"\n🎉 Done! {updated} files updated, {skipped} skipped.")
    print("\nNow go to GitHub Desktop and commit + push the changes.")
