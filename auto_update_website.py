#!/usr/bin/env python3
"""
Auto-Update Website with Viator Affiliate Links
Run this after GitHub Pages deployment to inject real affiliate URLs
"""
import json
import re
from datetime import datetime

def update_website_with_affiliates(website_url="https://YOUR_USERNAME.github.io/vacation-deals-site"):
    """
    Update the index.html with correct affiliate links after deployment.
    Call this after GitHub Pages is live.
    """
    
    # Load bundle data
    with open('/tmp/website_bundles.json', 'r') as f:
        bundles = json.load(f)
    
    print("="*80)
    print("🌐 WEBSITE AUTO-UPDATE - VIATOR AFFILIATE LINKS")
    print("="*80)
    print(f"\nWebsite URL: {website_url}")
    print(f"Bundles to update: {len(bundles)}")
    
    # Generate individual destination pages
    for bundle in bundles:
        slug = bundle['slug']
        html_content = f"""<!DOCTYPE html>
<html lang="en">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta http-equiv="refresh" content="2;url={bundle['viator_url']}">
    <title>{bundle['bundle_name']} - Experience Steals</title>
    <style>
        body {{
            font-family: -apple-system, BlinkMacSystemFont, 'Segoe UI', Roboto, sans-serif;
            background: linear-gradient(135deg, #667eea 0%, #764ba2 100%);
            color: white;
            display: flex;
            flex-direction: column;
            align-items: center;
            justify-content: center;
            height: 100vh;
            margin: 0;
            text-align: center;
            padding: 2rem;
        }}
        .emoji {{ font-size: 4rem; margin-bottom: 1rem; }}
        h1 {{ font-size: 2rem; margin-bottom: 0.5rem; }}
        .price {{ font-size: 2.5rem; font-weight: 800; margin: 1rem 0; }}
        .was {{ text-decoration: line-through; opacity: 0.7; font-size: 1.5rem; }}
        p {{ font-size: 1.1rem; opacity: 0.9; max-width: 400px; }}
        .loader {{
            margin-top: 2rem;
            width: 50px;
            height: 50px;
            border: 4px solid rgba(255,255,255,0.3);
            border-top-color: white;
            border-radius: 50%;
            animation: spin 1s linear infinite;
        }}
        @keyframes spin {{ to {{ transform: rotate(360deg); }} }}
    </style>
</head>
<body>
    <div class="emoji">{bundle['image_emoji']}</div>
    <h1>{bundle['bundle_name']}</h1>
    <p>{bundle['destination']}, {bundle['country']}</p>
    <div>
        <span class="was">${bundle['was']}</span>
        <div class="price">${bundle['price']}</div>
    </div>
    <p>{bundle['experience_count']} experiences included</p>
    <p>Taking you to Viator...</p>
    <div class="loader"></div>
</body>
</html>"""
        
        filename = f"/tmp/destination_pages/{slug}.html"
        import os
        os.makedirs("/tmp/destination_pages", exist_ok=True)
        
        with open(filename, 'w') as f:
            f.write(html_content)
    
    print(f"\n✅ Generated {len(bundles)} destination redirect pages")
    print(f"   Location: /tmp/destination_pages/")
    
    # Generate updated index.html
    print("\n📝 To update your website:")
    print("   1. Copy files from /tmp/destination_pages/ to your repo")
    print("   2. Update WEBSITE_URL in generate_bundle_posts.py")
    print("   3. Commit and push to GitHub")
    print("   4. Site will auto-update with all affiliate links")
    
    # Print sample post with correct URL
    sample = bundles[0]
    print(f"\n📱 Sample Instagram Post (after deployment):")
    print(f"""
POV: You got {sample['experience_count']} experiences in {sample['destination']} for ${sample['price']}

More bang for your buck.

✈️ {sample['destination']}, {sample['country']}
📦 {sample['bundle_name']}
💰 ${sample['price']} (was ${sample['was']})

👇 {website_url}/{sample['slug']}.html

#travel #experience #{sample['slug'].replace('-', '')} #adventure
""")
    
    print("="*80)

def generate_daily_post():
    """Generate today's post with direct affiliate link"""
    with open('/tmp/website_bundles.json', 'r') as f:
        bundles = json.load(f)
    
    import random
    bundle = random.choice(bundles)
    
    hooks = [
        f"POV: You got {bundle['experience_count']} experiences in {bundle['destination']} for ${bundle['price']}",
        f"POV: The {bundle['bundle_name']} is a STEAL at ${bundle['price']}",
        f"POV: Stop scrolling. ${bundle['price']} for ALL this in {bundle['destination']}?",
    ]
    
    caption_lines = [
        f"${bundle['price']} gets you {bundle['experience_count']} experiences.",
        "More bang for your buck.",
        f"That's ${int(bundle['price']/bundle['experience_count'])} per experience.",
    ]
    
    tier_emojis = {'platinum': '💎', 'gold': '🥇', 'silver': '🥈'}
    includes_text = "\n".join([f"✓ {item}" for item in bundle['includes'][:4]])
    
    caption = f"""{random.choice(hooks)}

{random.choice(caption_lines)}

✈️ {bundle['destination']}, {bundle['country']}
📦 {bundle['bundle_name']}
💰 ${bundle['price']} (was ${bundle['was']})
{tier_emojis[bundle['tier']]} {bundle['tier'].title()} Bundle

What's included:
{includes_text}

👇 Link in bio

#travel #experience #{bundle['slug'].replace('-', '')} #adventure #bundle"""
    
    print("="*80)
    print("📱 TODAY'S INSTAGRAM POST")
    print("="*80)
    print(caption)
    print("\n" + "="*80)
    
    # Save for reference
    with open('/tmp/today_post.txt', 'w') as f:
        f.write(caption)
    
    print("✅ Saved to /tmp/today_post.txt")
    return bundle

if __name__ == '__main__':
    import sys
    
    if len(sys.argv) > 1 and sys.argv[1] == 'daily':
        generate_daily_post()
    else:
        # Default: show update instructions
        website_url = sys.argv[1] if len(sys.argv) > 1 else "https://YOUR_USERNAME.github.io/vacation-deals-site"
        update_website_with_affiliates(website_url)
