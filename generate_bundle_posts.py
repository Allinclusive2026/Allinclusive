#!/usr/bin/env python3
"""
Vacation Bot - USA + International Bundle Deals
More bang for your buck - multiple experiences per destination
"""
import json
import random
from datetime import datetime

# Viator doesn't do flights, but we bundle multiple experiences for "more bang for buck"
# USA Domestic + International destinations
bundles = {
    # USA DOMESTIC - New additions
    'vegas': {
        'location': 'Las Vegas',
 'country': 'USA',
        'price': 599,
        'was': 1099,
        'tier': 'silver',
        'tagline': 'Ultimate Vegas Experience',
        'experiences': [
            'Helicopter tour over the Strip at night',
            'Grand Canyon day trip with Skywalk',
            'High roller observation wheel',
            'Cirque du Soleil show ticket',
            'Food tour of celebrity chef restaurants',
            'Neon museum vintage sign tour'
        ],
        'includes': [
            '4 nights on Strip hotel',
            'Helicopter night tour',
            'Grand Canyon day trip',
            'Show ticket included',
            'VIP club access'
        ],
        'vibe': 'neon lights + desert adventures + entertainment',
        'music_search': 'trending audio - nightlife/party'
    },
    'nyc': {
        'location': 'New York City',
        'country': 'USA',
        'price': 799,
        'was': 1399,
        'tier': 'gold',
        'tagline': 'NYC Bucket List Bundle',
        'experiences': [
            'Skip-line Statue of Liberty & Ellis Island',
            'Empire State Building sunrise access',
            'Food tour of Chelsea Market & Little Italy',
            'Brooklyn Bridge sunset bike ride',
            'Broadway show ticket (Orchestra)',
            'Central Park horse carriage ride'
        ],
        'includes': [
            '5 nights Manhattan hotel',
            'Statue of Liberty priority access',
            'Empire State Building',
            'Broadway show ticket',
            'Food tour included'
        ],
        'vibe': 'iconic sights + food culture + Broadway magic',
        'music_search': 'trending audio - nyc/urban'
    },
    'miami': {
        'location': 'Miami',
        'country': 'USA',
        'price': 549,
        'was': 999,
        'tier': 'silver',
        'tagline': 'South Beach & Everglades',
        'experiences': [
            'Everglades airboat adventure + gator show',
            'Wynwood Walls street art tour',
            'South Beach foodie walking tour',
            'Key West day trip with snorkeling',
            'Sunset yacht cruise with drinks',
            'Little Havana Cuban culture tour'
        ],
        'includes': [
            '4 nights South Beach hotel',
            'Everglades airboat tour',
            'Key West day trip',
            'Sunset cruise',
            'Food tour included'
        ],
        'vibe': 'beach vibes + wild everglades + Cuban culture',
        'music_search': 'trending audio - tropical/latin'
    },
    'la': {
        'location': 'Los Angeles',
        'country': 'USA',
        'price': 649,
        'was': 1199,
        'tier': 'silver',
        'tagline': 'Hollywood to Beach Bundle',
        'experiences': [
            'Warner Bros Studio Tour (real sets)',
            'Celebrity homes tour in Beverly Hills',
            'Santa Monica Pier sunset',
            'Griffith Observatory night tour',
            'Taco tour of Grand Central Market',
            'Venice Beach bike rental'
        ],
        'includes': [
            '4 nights Hollywood hotel',
            'Studio tour tickets',
            'Celebrity homes tour',
            'Observatory night access',
            'Bike rental included'
        ],
        'vibe': 'Hollywood glamour + beach sunsets + food scene',
        'music_search': 'trending audio - california/vibes'
    },
    'new_orleans': {
        'location': 'New Orleans',
        'country': 'USA',
        'price': 499,
        'was': 899,
        'tier': 'silver',
        'tagline': 'Jazz, Food & French Quarter',
        'experiences': [
            'Steamboat Natchez jazz cruise on Mississippi',
            'Cemetery/voodoo walking tour',
            'Cajun cooking class with chef',
            'Live jazz on Frenchman Street',
            'Swamp boat tour with gators',
            'Beignets at Cafe du Monde sunrise'
        ],
        'includes': [
            '4 nights French Quarter hotel',
            'Jazz river cruise',
            'Swamp tour',
            'Cooking class',
            'Cemetery tour'
        ],
        'vibe': 'jazz music + creole food + historic mystique',
        'music_search': 'trending audio - jazz/new orleans'
    },
    'san_francisco': {
        'location': 'San Francisco',
        'country': 'USA',
        'price': 699,
        'was': 1299,
        'tier': 'gold',
        'tagline': 'Golden Gate to Wine Country',
        'experiences': [
            'Alcatraz Island night tour',
            'Muir Woods redwoods hike',
            'Napa Valley wine tasting day trip',
            'Cable car passes (3-day)',
            'Fisherman\'s Wharf food tour',
            'Sunset sail under Golden Gate'
        ],
        'includes': [
            '4 nights downtown hotel',
            'Alcatraz night tour',
            'Napa wine country day trip',
            'Cable car passes',
            'Sunset bay cruise'
        ],
        'vibe': 'iconic bridges + redwoods + wine country',
        'music_search': 'trending audio - chill/california'
    },
    'chicago': {
        'location': 'Chicago',
        'country': 'USA',
        'price': 449,
        'was': 799,
        'tier': 'silver',
        'tagline': 'Architecture & Deep Dish',
        'experiences': [
            'Architecture river cruise (best in US)',
            'Deep dish pizza making class',
            '360 Chicago tilt experience',
            'Millennium Park & Cloud Gate tour',
            'Navy Pier fireworks cruise',
            'Blues club hop on South Side'
        ],
        'includes': [
            '3 nights Downtown hotel',
            'Architecture boat tour',
            'Pizza making class',
            '360 Chicago observation',
            'Blues club tour'
        ],
        'vibe': 'architecture marvels + blues music + deep dish',
        'music_search': 'trending audio - urban/explore'
    },
    # INTERNATIONAL - Updated with bundles
    'cancun': {
        'location': 'Cancun',
        'country': 'Mexico',
        'price': 699,
        'was': 1299,
        'tier': 'silver',
        'tagline': 'Mayan Wonders Bundle',
        'experiences': [
            'Chichen Itza sunrise with archaeologist',
            'Cenote swimming (underground caves)',
            'Snorkeling with sea turtles in Akumal',
            'Isla Mujeres catamaran + lunch',
            'Mayan cooking class with family',
            'ATV jungle adventure'
        ],
        'includes': [
            '5 nights beach hotel',
            'Chichen Itza tour',
            'Cenote experience',
            'Isla Mujeres day trip',
            'Turtle snorkeling'
        ],
        'vibe': 'ancient ruins + crystal water + jungle adventures',
        'music_search': 'trending audio - adventure/explore'
    },
    'rome': {
        'location': 'Rome',
        'country': 'Italy',
        'price': 899,
        'was': 1599,
        'tier': 'gold',
        'tagline': 'Ancient Rome Immersion',
        'experiences': [
            'Skip-line Vatican & Sistine Chapel',
            'Pasta-making with Italian nonna',
            'Colosseum underground + arena floor',
            'Vespa night tour through Trastevere',
            'Ancient Rome walking tour',
            'Tuscan wine day trip'
        ],
        'includes': [
            '5 nights central Rome',
            'Vatican skip-the-line',
            'Cooking class',
            'Colosseum full access',
            'Day trip to Tuscany'
        ],
        'vibe': 'ancient history + authentic food + culture',
        'music_search': 'trending audio - europe/travel'
    },
    'bali': {
        'location': 'Bali',
        'country': 'Indonesia',
        'price': 899,
        'was': 1599,
        'tier': 'gold',
        'tagline': 'Temples & Traditions Bundle',
        'experiences': [
            'Sacred Monkey Forest sunrise',
            'Traditional Balinese cooking class',
            'Mt. Batur sunrise volcano trek',
            'Temple purification ceremony',
            'Tegalalang rice terrace trekking',
            'Sunset at Tanah Lot temple'
        ],
        'includes': [
            '7 nights Ubud villa',
            'Volcano sunrise trek',
            'Cooking class',
            'Purification ceremony',
            'Temple tours'
        ],
        'vibe': 'temples + jungle + spiritual experiences',
        'music_search': 'trending audio - chill/relaxing'
    },
    'costa_rica': {
        'location': 'Costa Rica',
        'country': 'Costa Rica',
        'price': 799,
        'was': 1499,
        'tier': 'gold',
        'tagline': 'Wildlife Adventure Package',
        'experiences': [
            'Zip-lining through cloud forests',
            'Sloth sanctuary volunteer day',
            'Night jungle walk with biologist',
            'Arenal volcano hot springs',
            'Coffee plantation tour',
            'White water rafting'
        ],
        'includes': [
            '6 nights eco-lodge',
            'Cloud forest zip-lining',
            'Sloth sanctuary',
            'Night jungle tour',
            'Hot springs'
        ],
        'vibe': 'wildlife + adventure + nature immersion',
        'music_search': 'trending audio - adventure/explore'
    },
    'japan': {
        'location': 'Japan',
        'country': 'Japan',
        'price': 1899,
        'was': 3200,
        'tier': 'platinum',
        'tagline': 'Cultural Immersion Experience',
        'experiences': [
            'Traditional tea ceremony in temple',
            'Sushi-making at Tsukiji market',
            'Bullet train to Mt. Fuji',
            'Fushimi Inari shrine hike',
            'Samurai sword experience',
            'Onsen hot spring tradition'
        ],
        'includes': [
            '7 nights Tokyo/Kyoto',
            'Tea ceremony',
            'Cooking class',
            'JR Pass',
            'Guided tours'
        ],
        'vibe': 'tradition meets modern + culture deep dive',
        'music_search': 'trending audio - japan/travel'
    },
    'egypt': {
        'location': 'Egypt',
        'country': 'Egypt',
        'price': 1299,
        'was': 2400,
        'tier': 'platinum',
        'tagline': 'Pyramids & Nile Adventure',
        'experiences': [
            'Private pyramid sunrise with Egyptologist',
            'Nile felucca sunset sailing',
            'Hot air balloon over Luxor',
            'Valley of the Kings exploration',
            'Khan el-Khalili bazaar tour',
            'Camel trek to Bedouin camp'
        ],
        'includes': [
            '7 nights boutique hotels',
            'Private Egyptologist',
            'Hot air balloon',
            'Nile cruise',
            'All entrance fees'
        ],
        'vibe': 'ancient wonders + desert magic + history',
        'music_search': 'trending audio - epic/adventure'
    },
    'peru': {
        'location': 'Peru',
        'country': 'Peru',
        'price': 1099,
        'was': 1999,
        'tier': 'platinum',
        'tagline': 'Inca Trail Expedition',
        'experiences': [
            '4-day Inca Trail trek to Machu Picchu',
            'Rainbow Mountain sunrise hike',
            'Sacred Valley ATV adventure',
            'Traditional weaving workshop',
            'Cusco food market tour',
            'Pisco sour making class'
        ],
        'includes': [
            '4-day Inca Trail trek',
            'Professional guides',
            'Rainbow Mountain',
            'All camping gear',
            'Machu Picchu entry'
        ],
        'vibe': 'ancient civilization + mountain adventures',
        'music_search': 'trending audio - adventure/epic'
    },
    'morocco': {
        'location': 'Morocco',
        'country': 'Morocco',
        'price': 849,
        'was': 1599,
        'tier': 'gold',
        'tagline': 'Sahara Desert Escape',
        'experiences': [
            'Sahara camel trek + overnight camp',
            'Medina food tour Marrakech',
            'Traditional hammam spa',
            'Atlas Mountains Berber village',
            'Fez leather tannery tour',
            'Majorelle Garden sunrise'
        ],
        'includes': [
            '6 nights riads + camp',
            'Sahara overnight trek',
            'Hammam spa',
            'Atlas Mountains',
            'Fez tour'
        ],
        'vibe': 'desert magic + colorful markets + culture',
        'music_search': 'trending audio - exotic/travel'
    },
    'greece': {
        'location': 'Greece',
        'country': 'Greece',
        'price': 1099,
        'was': 1899,
        'tier': 'platinum',
        'tagline': 'Islands & Ancient Wonders',
        'experiences': [
            'Acropolis sunrise with archaeologist',
            'Santorini catamaran sunset cruise',
            'Greek island ferry hopping',
            'Athens food walking tour',
            'Volcanic vineyard wine tasting',
            'Oia to Fira cliff hike'
        ],
        'includes': [
            '5 nights Athens/Santorini',
            'Acropolis guided tour',
            'Catamaran cruise',
            'Wine tasting',
            'Ferry tickets'
        ],
        'vibe': 'ancient history + Mediterranean beauty',
        'music_search': 'trending audio - summer/vibes'
    },
    'thailand': {
        'location': 'Thailand',
        'country': 'Thailand',
        'price': 749,
        'was': 1399,
        'tier': 'silver',
        'tagline': 'Temples & Elephant Sanctuary',
        'experiences': [
            'Floating market boat tour',
            'Elephant sanctuary volunteer',
            'Thai street food night tour',
            'Temple hopping by tuk-tuk',
            'Traditional massage course',
            'Organic farm cooking class'
        ],
        'includes': [
            '6 nights Bangkok/Chiang Mai',
            'Elephant sanctuary',
            'Floating market',
            'Cooking class',
            'Temple tours'
        ],
        'vibe': 'temples + street food + tropical vibes',
        'music_search': 'trending audio - tropical/chill'
    },
    'iceland': {
        'location': 'Iceland',
        'country': 'Iceland',
        'price': 1199,
        'was': 2199,
        'tier': 'platinum',
        'tagline': 'Northern Lights & Glaciers',
        'experiences': [
            'Northern Lights jeep chase',
            'Blue Lagoon geothermal spa',
            'Golden Circle waterfall trek',
            'Glacier hiking expedition',
            'Black sand beach exploration',
            'Whale watching cruise'
        ],
        'includes': [
            '5 nights Reykjavik',
            'Aurora jeep tour',
            'Blue Lagoon',
            'Glacier hike',
            'Whale watching'
        ],
        'vibe': 'otherworldly landscapes + nature wonders',
        'music_search': 'trending audio - cinematic/epic'
    },
    'new_zealand': {
        'location': 'New Zealand',
        'country': 'New Zealand',
        'price': 1499,
        'was': 2799,
        'tier': 'platinum',
        'tagline': 'Adventure Capital Package',
        'experiences': [
            'Milford Sound fjord cruise',
            'Bungee jumping Kawarau Bridge',
            'Hobbiton movie set tour',
            'Glowworm caves kayak',
            'Maori cultural performance',
            'Skydiving over Lake Wakatipu'
        ],
        'includes': [
            '6 nights Queenstown/Auckland',
            'Milford Sound cruise',
            'Hobbiton tour',
            'Maori feast',
            'Adventure activities'
        ],
        'vibe': 'adrenaline + cinematic landscapes',
        'music_search': 'trending audio - adventure/epic'
    }
}

def generate_pov_scenes(location, country, experiences, vibe):
    """Generate 8 POV scenes with hands/feet in frame"""
    
    hand_types = [
        "brown hands", "Black hands", "tan hands", "golden-brown hands",
        "diverse hands", "tattooed hands", "henna-decorated hands",
        "weathered hands", "young hands", "aged hands"
    ]
    
    person_types = [
        "solo traveler", "couple", "group of friends",
        "Black woman", "South Asian man", "Latina woman",
        "mixed-race couple", "elderly adventurer", "young explorer"
    ]
    
    hand = random.choice(hand_types)
    person = random.choice(person_types)
    
    # Pick 2-3 experiences to highlight in scenes
    highlight_experiences = random.sample(experiences, min(3, len(experiences)))
    
    scenes = {
        1: {
            'prompt': f"POV: {hand} zipping up backpack in hotel room, boarding passes on bed, early morning excitement, {location} trip",
            'duration': 3
        },
        2: {
            'prompt': f"POV: {hand} pulling rolling suitcase through busy airport terminal, motion blur, ready for {location}",
            'duration': 3
        },
        3: {
            'prompt': f"POV: {hand} holding passport at gate, {location} destination on boarding pass, anticipation",
            'duration': 3
        },
        4: {
            'prompt': f"POV: {hand} lifting airplane window shade, first glimpse of {location} landscape below",
            'duration': 4
        },
        5: {
            'prompt': f"POV: {hand} holding tickets at {location} attraction entrance, {highlight_experiences[0]} in background",
            'duration': 4
        },
        6: {
            'prompt': f"POV: {hand} reaching out to touch/feel experience at {location}, {highlight_experiences[1]}, awe moment",
            'duration': 4
        },
        7: {
            'prompt': f"POV: {person}'s feet walking unique terrain at {location} - {vibe}, immersive ground-level",
            'duration': 4
        },
        8: {
            'prompt': f"POV: {hand} holding phone capturing epic moment at {location}, {highlight_experiences[2] if len(highlight_experiences) > 2 else highlight_experiences[0]}, pure joy",
            'duration': 5
        }
    }
    
    return scenes

def generate_bundle_post(bundle_key):
    """Generate Instagram post with bundle focus"""
    bundle = bundles[bundle_key]
    
    # Hooks focused on VALUE - multiple experiences
    hooks = [
        f"POV: You got {len(bundle['experiences'])} experiences in {bundle['location']} for ${bundle['price']}",
        f"POV: The {bundle['tagline']} is a STEAL at ${bundle['price']}",
        f"POV: You said yes to {bundle['location']} and got ALL of this",
        f"POV: Stop scrolling. ${bundle['price']} for ALL this in {bundle['location']}?",
        f"POV: You finally stopped waiting and booked the {bundle['tagline']}",
        f"POV: Your hands holding {len(bundle['experiences'])} different tickets in {bundle['location']}"
    ]
    
    caption_lines = [
        f"${bundle['price']} gets you {len(bundle['experiences'])} experiences.",
        "More bang for your buck.",
        "Everything included. No hidden fees.",
        "Book the bundle.",
        f"That's ${int(bundle['price']/len(bundle['experiences']))} per experience.",
    ]
    
    tier_emojis = {'platinum': '💎', 'gold': '🥇', 'silver': '🥈'}
    
    # Format includes list
    includes_text = "\n".join([f"✓ {item}" for item in bundle['includes'][:4]])
    
    caption = f"""{random.choice(hooks)}

{random.choice(caption_lines)}

✈️ {bundle['location']}, {bundle['country']}
📦 {bundle['tagline']}
💰 ${bundle['price']} (was ${bundle['was']})
{tier_emojis[bundle['tier']]} {bundle['tier'].title()} Bundle

What's included:
{includes_text}

👇 Link in bio to book

#travel #experience #{bundle_key.replace('_', '')} #adventure #bundle"""
    
    # Generate POV scenes
    scenes = generate_pov_scenes(
        bundle['location'], 
        bundle['country'],
        bundle['experiences'],
        bundle['vibe']
    )
    
    return {
        'destination': bundle['location'],
        'country': bundle['country'],
        'bundle_name': bundle['tagline'],
        'experience_count': len(bundle['experiences']),
        'price': bundle['price'],
        'was': bundle['was'],
        'tier': bundle['tier'],
        'experiences': bundle['experiences'],
        'includes': bundle['includes'],
        'caption': caption,
        'hook': random.choice(hooks),
        'pov_scenes': scenes,
        'total_duration': sum(s['duration'] for s in scenes.values()),
        'music_search': bundle['music_search'],
        'vibe': bundle['vibe'],
        'viator_url': f"https://www.viator.com/searchResults/all?destination={bundle['location'].replace(' ', '%20')}&mcid=28353",
        'editing_notes': {
            'style': 'POV first-person, handheld camera feel',
            'diversity': 'Mixed representation - hands/feet varied skin tones',
            'pacing': 'Quick cuts (3-5s), speed ramp transitions',
            'music': f"Search IG: {bundle['music_search']}",
            'text_overlay': f'"{random.choice(caption_lines)}" at scene 5',
            'color_grade': 'Match destination vibe'
        }
    }

def main():
    print("="*80)
    print("🎒 BUNDLE DEALS - USA + INTERNATIONAL")
    print("More bang for your buck | Multiple experiences per destination")
    print("="*80)
    
    all_posts = []
    
    # Separate USA vs International for reporting
    usa_bundles = {k: v for k, v in bundles.items() if v['country'] == 'USA'}
    intl_bundles = {k: v for k, v in bundles.items() if v['country'] != 'USA'}
    
    print(f"\n🇺🇸 USA DOMESTIC: {len(usa_bundles)} destinations")
    print(f"🌍 INTERNATIONAL: {len(intl_bundles)} destinations")
    print(f"TOTAL: {len(bundles)} bundle deals")
    
    for bundle_key in bundles:
        post = generate_bundle_post(bundle_key)
        all_posts.append(post)
        
        print(f"\n{'='*80}")
        print(f"{post['tier'].upper()}: {post['destination']} ({post['country']}) - ${post['price']}")
        print(f"Bundle: {post['bundle_name']}")
        print(f"Experiences: {post['experience_count']}")
        print(f"Hook: {post['hook'][:70]}...")
    
    # Save all posts
    with open('/tmp/vacation_bundle_posts.json', 'w') as f:
        json.dump(all_posts, f, indent=2)
    
    # Generate today's content
    today_bundle = random.choice(list(bundles.keys()))
    today_post = generate_bundle_post(today_bundle)
    
    kling_output = f"""🎬 TODAY'S BUNDLE: {today_post['destination'].upper()}
Bundle: {today_post['bundle_name']}
Experiences: {today_post['experience_count']}
Price: ${today_post['price']}
Hook: {today_post['hook']}

COPY THESE 8 PROMPTS TO KLING-03 (POE):

"""
    for num, scene in today_post['pov_scenes'].items():
        kling_output += f"""
Scene {num} ({scene['duration']} seconds):
{scene['prompt']}

"""
    
    kling_output += f"""
CAPTION:
{today_post['caption']}

VIATOR AFFILIATE URL:
{today_post['viator_url']}

EDITING NOTES:
- Style: {today_post['editing_notes']['style']}
- Music: {today_post['editing_notes']['music']}
- Text overlay: {today_post['editing_notes']['text_overlay']}
"""
    
    with open('/tmp/vacation_kling_today.txt', 'w') as f:
        f.write(kling_output)
    
    # Create website-ready JSON with affiliate links
    website_data = []
    for post in all_posts:
        website_data.append({
            'slug': post['destination'].lower().replace(' ', '-'),
            'destination': post['destination'],
            'country': post['country'],
            'bundle_name': post['bundle_name'],
            'price': post['price'],
            'was': post['was'],
            'tier': post['tier'],
            'experience_count': post['experience_count'],
            'experiences': post['experiences'],
            'includes': post['includes'],
            'viator_url': post['viator_url'],
            'image_emoji': {'USA': '🇺🇸', 'Italy': '🏛️', 'Mexico': '🐢', 'Indonesia': '🛕', 
                           'Costa Rica': '🦥', 'Japan': '🗾', 'Egypt': '🏛️', 'Peru': '⛰️',
                           'Morocco': '🏜️', 'Greece': '🏛️', 'Thailand': '🐘', 
                           'Iceland': '🌌', 'New Zealand': '⛰️'}.get(post['country'], '✈️')
        })
    
    with open('/tmp/website_bundles.json', 'w') as f:
        json.dump(website_data, f, indent=2)
    
    print("\n" + "="*80)
    print("✅ Posts saved to /tmp/vacation_bundle_posts.json")
    print("🎬 Today's Kling prompts: /tmp/vacation_kling_today.txt")
    print("🌐 Website data: /tmp/website_bundles.json (ready for auto-post)")
    print("\n🎯 BUNDLE STRATEGY:")
    print(f"   • {len(bundles)} destinations total")
    print(f"   • {len(usa_bundles)} USA domestic (Vegas, NYC, Miami, LA, NOLA, SF, Chicago)")
    print(f"   • {len(intl_bundles)} International")
    print("   • 4-7 experiences per bundle")
    print("   • 'More bang for your buck' messaging")
    print("   • Viator affiliate links ready for auto-post")
    print("="*80)

if __name__ == '__main__':
    main()
