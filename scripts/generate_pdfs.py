from pathlib import Path
from reportlab.lib.pagesizes import A4
from reportlab.lib.colors import HexColor, Color
from reportlab.pdfgen import canvas
from reportlab.platypus import Paragraph
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.enums import TA_LEFT, TA_CENTER
from reportlab.lib.utils import ImageReader
from reportlab.lib.units import mm
from PIL import Image

ROOT = Path(__file__).resolve().parents[1]
PUBLIC = ROOT / 'public'
PRODUCT = ROOT / 'product-files'

PAGE_W, PAGE_H = A4
MARGIN_X = 24 * mm
TOP_BAR_H = 18 * mm
BOTTOM_MARGIN = 20 * mm

NAVY = HexColor('#0B1531')
BLUE = HexColor('#0B6AFF')
GOLD = HexColor('#F8C13B')
CREAM = HexColor('#F6F3ED')
SLATE = HexColor('#4B5B73')
INK = HexColor('#111827')
CARD = HexColor('#EFF3F8')
BORDER = HexColor('#D8E0EA')
SOFT_GOLD = HexColor('#EEE5CD')
WHITE = HexColor('#FFFFFF')

styles = {
    'cover_eyebrow': ParagraphStyle('cover_eyebrow', fontName='Helvetica-Bold', fontSize=12, leading=14, textColor=WHITE),
    'cover_title': ParagraphStyle('cover_title', fontName='Helvetica-Bold', fontSize=28, leading=34, textColor=WHITE),
    'cover_body': ParagraphStyle('cover_body', fontName='Helvetica', fontSize=12.5, leading=17, textColor=WHITE),
    'body': ParagraphStyle('body', fontName='Helvetica', fontSize=10.8, leading=15, textColor=SLATE),
    'body_small': ParagraphStyle('body_small', fontName='Helvetica', fontSize=9.6, leading=12.5, textColor=SLATE),
    'card_title': ParagraphStyle('card_title', fontName='Helvetica-Bold', fontSize=12, leading=14, textColor=INK),
    'small_caps': ParagraphStyle('small_caps', fontName='Helvetica-Bold', fontSize=9.6, leading=11, textColor=SLATE),
    'page_title': ParagraphStyle('page_title', fontName='Helvetica-Bold', fontSize=25, leading=28, textColor=INK),
    'page_sub': ParagraphStyle('page_sub', fontName='Helvetica', fontSize=12, leading=15, textColor=SLATE),
    'section_title': ParagraphStyle('section_title', fontName='Helvetica-Bold', fontSize=13.5, leading=16, textColor=INK),
    'footer': ParagraphStyle('footer', fontName='Helvetica', fontSize=9.5, leading=11, textColor=SLATE),
}

premium_days = [
    {
        'title': 'Day 1 - Castle District + Danube',
        'sub': 'The high-impact first-impression day',
        'intro': 'This day gives first-time visitors the postcard Budapest they imagined, but in a sequence that feels calmer than it looks on paper.',
        'blocks': [
            ('08:00', 'Fisherman\'s Bastion + Trinity Square', 'Start at Fisherman\'s Bastion before the terraces get crowded. If you want the upper paid areas, check the official site first.'),
            ('09:00', 'Matthias Church interior', 'Walk straight into Matthias Church if you want the interior. Hours vary, so confirm them on the official page or use the ticket page.'),
            ('10:15', 'Castle walls + photo walk', 'Continue through the Buda Castle courtyards and promenade side for panoramic river views. This is a good time to slow down and not overschedule a museum.'),
            ('12:15', 'Lunch anchor', 'Keep lunch in or near the Castle area so you do not waste the midday transition. Pest-Buda is a solid classic, but the point is to keep this meal local to the route.'),
            ('14:00', 'Cross to the riverfront', 'Use the funicular if it helps your pace, or walk down toward the Chain Bridge side and save your energy for the evening river stretch.'),
            ('18:30', 'Danube evening finish', 'Finish with a Danube-side walk or a cruise if that is one of your priority experiences. Keep this block open enough that sunset timing can lead the evening instead of the clock.'),
        ],
        'note_title': 'Local note',
        'note': 'Do not try to cram the National Gallery, Hospital in the Rock, and every lookout point into the same first day. Budapest lands better when the Castle District morning stays elegant instead of exhaustive.',
    },
    {
        'title': 'Day 2 - Parliament + Baths + Jewish Quarter',
        'sub': 'The classic Budapest contrast day',
        'intro': 'This route pairs ceremonial city highlights with a slower bath session and a lively evening. It works because the rhythm gets looser after lunch.',
        'blocks': [
            ('08:30', 'Parliament area first', 'Keep the morning precise. If Parliament is a priority, treat that reservation as the fixed point and let the riverfront walk flex around it.'),
            ('10:30', 'Shoes on the Danube + riverside walk', 'Stay on the Pest side after the morning booking so you keep the route coherent. The memorial and promenade are emotionally heavy, so keep the pace respectful.'),
            ('12:00', 'Lunch near the basilica', 'Use lunch as a reset between the formal city core and the afternoon bath block. This is also a good window for coffee if you booked a later bath slot.'),
            ('14:30', 'Széchenyi or Gellért bath block', 'Plan a real bath block, not a token dip. Budapest thermal culture rewards time, so leave enough space to change, soak, and recover.'),
            ('18:30', 'Jewish Quarter dinner', 'Re-enter the city through the Jewish Quarter so the energy naturally lifts after the baths. This is where the day becomes social again.'),
            ('21:00', 'Ruin bar finish', 'Pick one or two bars and stop while the night still feels crisp. The goal is atmosphere, not a checklist of venues.'),
        ],
        'note_title': 'Route logic',
        'note': 'Baths are best used as the day\'s slowdown, not squeezed between too many city-core landmarks. Build around the bath rather than trying to recover from the bath with more sightseeing.',
    },
    {
        'title': 'Day 3 - City Park + Andrássy + cafés',
        'sub': 'A spacious final core day',
        'intro': 'Day 3 should feel more breathable than the first two. This route keeps the architecture, museum options, and café moments without forcing another marathon.',
        'blocks': [
            ('09:00', 'Heroes\' Square arrival', 'Start at Heroes\' Square before the broad spaces feel fully exposed and crowded. It is the cleanest way to enter City Park.'),
            ('10:00', 'City Park choice block', 'Choose one main anchor here: Vajdahunyad exterior, House of Music Hungary, or Széchenyi if you skipped baths earlier. Keep one clear choice rather than partialing three.'),
            ('12:30', 'Lunch or pastry stop', 'Use the City Park to Andrássy transition for an easy lunch. If the weather is strong, this is a great time for a slower terrace meal.'),
            ('14:00', 'Andrássy Avenue descent', 'Walk or ride down Andrássy at a gentle pace, using the avenue as a connector rather than a list of stops. The payoff is the elegant transition back into the centre.'),
            ('16:00', 'Coffee + shopping window', 'Keep this open enough for a café break, design shop, or simply a rest hour. It makes the trip feel designed rather than over-optimized.'),
            ('19:00', 'Final dinner with a view or strong kitchen', 'End with your best dinner booking of the core trip. This is the night to spend slightly more for the memory.'),
        ],
        'note_title': 'Rainy-day backup',
        'note': 'If the weather turns, use an indoor anchor like the House of Terror, House of Music Hungary, or a longer café session and keep Andrássy as a transit corridor instead of a promenade.',
    },
    {
        'title': 'Day 4 - Szentendre add-on',
        'sub': 'A lower-pressure day-trip extension',
        'intro': 'Szentendre works best as a slower creative detour. Use it if you want art streets, a different pace, and a break from the capital\'s heavier city grid.',
        'blocks': [
            ('09:00', 'Travel north on the H5', 'Depart in the morning so the town still feels quiet on arrival. Keep the transport simple and do not over-plan individual museums.'),
            ('10:00', 'Old town stroll', 'Walk the small streets first and choose only the stops that naturally pull you in. The experience is the atmosphere, not the punch-list.'),
            ('12:30', 'Lunch by the centre or river', 'Take a proper lunch and use the midday break to decide whether you want galleries, marzipan, or just coffee and browsing.'),
            ('15:00', 'Optional museum or river stretch', 'If the weather is good, choose the river edge. If not, step into one museum or church rather than trying to collect several.'),
            ('18:00', 'Return to Budapest', 'Come back early enough that the evening still feels open. This extension should freshen the trip, not drain it.'),
        ],
        'note_title': 'Best use case',
        'note': 'Take the Szentendre extension when you want breathing room, not because you feel obliged to leave Budapest. It is a quality-of-trip decision, not a quantity-of-sights decision.',
    },
    {
        'title': 'Day 5 - Great Synagogue + food-led finish',
        'sub': 'An urban final day with a human scale',
        'intro': 'This closing day focuses on the Jewish Quarter, the Great Synagogue area, and food. It is intentionally less monumental and more lived-in.',
        'blocks': [
            ('10:00', 'Great Synagogue area', 'Anchor the morning around the synagogue and the surrounding streets. This gives the day both a cultural centre and a clear emotional tone.'),
            ('12:00', 'Market or casual lunch', 'Keep lunch practical and flavour-led. Street-food courts or modern Hungarian spots both work well here.'),
            ('14:00', 'Design shops + coffee loop', 'Use the afternoon for lighter browsing, coffee, and last purchases. It keeps the final day mobile and flexible.'),
            ('17:00', 'Golden-hour neighborhood walk', 'Let the neighborhood itself be the experience. The point is to finish with atmosphere and good energy rather than one last heavy ticketed stop.'),
            ('20:00', 'Choose your final night', 'You can go elegant, casual, or social. Decide whether you want closure, celebration, or one last Budapest street-energy night and book accordingly.'),
        ],
        'note_title': 'Best for',
        'note': 'This extension is especially good for couples, repeat café people, and travelers who prefer finishing a trip in a neighborhood mood rather than at a giant attraction.',
    },
]

official_links = [
    ('BudapestGO', 'Digital tickets, route planning, and airport bus 100E purchases.', 'https://bkk.hu/en/tickets-and-passes/budapestgo/'),
    ('Parliament', 'Visitor information, timed tours, and official purchase flow.', 'https://www.parlament.hu/web/visitors'),
    ('Szechenyi Thermal Bath', 'Current opening hours, ticket flow, and visitor FAQs.', 'https://www.szechenyibath.hu/'),
    ('Matthias Church', 'Current church access and ticket details in the Castle District.', 'https://matyas-templom.hu/en/'),
    ('Great Synagogue', 'Useful for current visitor information in the Jewish Quarter.', 'https://dohany-zsinagoga.hu/'),
]

food_lists = [
    ('Food anchors', ['Castle District lunch: keep it compact and local to the route.', 'Pest centre coffee stop: use a proper café reset instead of a rushed snack.', 'Jewish Quarter dinner: reserve one stronger dinner rather than grazing everywhere.']),
    ('Neighborhood notes', ['Castle District is at its best in the morning.', 'Parliament + basilica zone works well for a cleaner midday.', 'Jewish Quarter carries the evening energy best.', 'City Park needs fewer stops than first-time visitors assume.']),
    ('Rainy-day backups', ['Bath block + café session', 'House of Music Hungary or another indoor design/culture anchor', 'Longer market lunch and reduced walking route']),
]

checklist_sections = [
    ('Before you fly', [
        'Save your accommodation address offline and screenshot your arrival route from the airport.',
        'Download BudapestGO before departure if you plan to use public transport frequently.',
        'Book time-sensitive highlights like Parliament or Szechenyi before you lock the rest of your days.',
    ]),
    ('Carry-on and daily bag essentials', [
        'Passport or ID, payment card, and a little backup cash.',
        'Power bank, charging cable, and the adapter you actually need.',
        'Comfortable walking shoes and one light weather layer.',
        'Reusable water bottle and small tissues pack.',
        'Offline copy of your itinerary PDF and any ticket confirmations.',
        'Compact umbrella if the forecast looks unstable.',
    ]),
    ('City-ready habits', [
        'Keep one calm breakfast slot in the plan each day.',
        'Use the bath day as the recovery day, not as a packed sightseeing day.',
        'Do not overbook the Castle District and Parliament on the same morning.',
        'Save one flexible dinner slot for a spontaneous neighborhood choice.',
    ]),
    ('Useful final checks', [
        'Confirm airport transfer plan the night before departure.',
        'Check official attraction pages if you are relying on a specific timed ticket.',
        'Wear layers - Budapest can feel cooler by the river after sunset even on otherwise warm days.',
        'Keep your final day lighter than your first three. The city rewards pacing.',
    ]),
]

def crop_cover(path: Path) -> Image.Image:
    img = Image.open(path).convert('RGB')
    target_ratio = PAGE_W / PAGE_H
    w, h = img.size
    src_ratio = w / h
    if src_ratio > target_ratio:
        new_w = int(h * target_ratio)
        left = (w - new_w) // 2
        img = img.crop((left, 0, left + new_w, h))
    else:
        new_h = int(w / target_ratio)
        top = (h - new_h) // 2
        img = img.crop((0, top, w, top + new_h))
    img = img.resize((int(PAGE_W), int(PAGE_H)))
    overlay = Image.new('RGB', img.size, '#0B1531')
    img = Image.blend(img, overlay, 0.42)
    return img


def pdraw(c, text, style, x, top_y, width):
    para = Paragraph(text, style)
    w, h = para.wrap(width, 10_000)
    para.drawOn(c, x, top_y - h)
    return h


def round_box(c, x, y, w, h, fill=CARD, stroke=BORDER, radius=16, line=1):
    c.setFillColor(fill)
    c.setStrokeColor(stroke)
    c.setLineWidth(line)
    c.roundRect(x, y, w, h, radius, fill=1, stroke=1)


def header_bar(c, page_num, title='Budapest itinerary'):
    c.setFillColor(NAVY)
    c.rect(0, PAGE_H - TOP_BAR_H, PAGE_W, TOP_BAR_H, fill=1, stroke=0)
    c.setFillColor(WHITE)
    c.setFont('Helvetica-Bold', 12)
    c.drawString(MARGIN_X, PAGE_H - 12*mm, 'PearlZone')
    c.setFont('Helvetica', 11)
    label = f'{title}  ·  page {page_num}'
    tw = c.stringWidth(label, 'Helvetica', 11)
    c.drawString(PAGE_W - MARGIN_X - tw, PAGE_H - 12*mm, label)


def footer(c, left='pearlzone.hu', right='Save the PDF offline before you fly.'):
    y = 15 * mm
    c.setStrokeColor(BORDER)
    c.setLineWidth(1)
    c.line(MARGIN_X, y + 12, PAGE_W - MARGIN_X, y + 12)
    c.setFillColor(SLATE)
    c.setFont('Helvetica', 10)
    c.drawString(MARGIN_X, y - 8, left)
    tw = c.stringWidth(right, 'Helvetica', 10)
    c.drawString(PAGE_W - MARGIN_X - tw, y - 8, right)


def chip(c, x, y, text):
    c.setFont('Helvetica-Bold', 11)
    w = c.stringWidth(text, 'Helvetica-Bold', 11) + 20
    c.setFillColor(Color(1,1,1, alpha=0.08))
    c.setStrokeColor(Color(1,1,1, alpha=0.35))
    c.roundRect(x, y, w, 22, 11, fill=1, stroke=1)
    c.setFillColor(WHITE)
    c.drawString(x + 10, y + 6.5, text)
    return w


def draw_timeline_page(c, page_num, spec):
    c.setFillColor(CREAM)
    c.rect(0, 0, PAGE_W, PAGE_H, fill=1, stroke=0)
    header_bar(c, page_num)
    top = PAGE_H - TOP_BAR_H - 16*mm
    pdraw(c, spec['title'], styles['page_title'], MARGIN_X, top, PAGE_W - 2*MARGIN_X)
    pdraw(c, spec['sub'], styles['page_sub'], MARGIN_X, top - 19*mm, PAGE_W - 2*MARGIN_X)
    pdraw(c, spec['intro'], styles['body'], MARGIN_X, top - 34*mm, PAGE_W - 2*MARGIN_X)

    y_top = top - 70*mm
    box_h = 19 * mm
    gap = 4 * mm
    for idx, (time, title, body) in enumerate(spec['blocks']):
        y = y_top - idx * (box_h + gap)
        # time pill
        c.setFillColor(SOFT_GOLD)
        c.setStrokeColor(SOFT_GOLD)
        c.roundRect(MARGIN_X, y + 1*mm, 24*mm, 8*mm, 7, fill=1, stroke=0)
        c.setFillColor(INK)
        c.setFont('Helvetica-Bold', 10)
        c.drawCentredString(MARGIN_X + 12*mm, y + 4.2, time)
        # card
        round_box(c, MARGIN_X + 30*mm, y - 3*mm, PAGE_W - 2*MARGIN_X - 30*mm, box_h, fill=Color(1,1,1, alpha=0.42), stroke=BORDER, radius=18)
        pdraw(c, title, styles['card_title'], MARGIN_X + 34*mm, y + 13*mm, PAGE_W - 2*MARGIN_X - 38*mm)
        pdraw(c, body, styles['body_small'], MARGIN_X + 34*mm, y + 5.4*mm, PAGE_W - 2*MARGIN_X - 38*mm)

    note_y = 34*mm
    round_box(c, MARGIN_X, note_y, PAGE_W - 2*MARGIN_X, 30*mm, fill=HexColor('#E8ECF2'), stroke=BORDER, radius=16)
    pdraw(c, spec['note_title'], styles['card_title'], MARGIN_X + 6*mm, note_y + 24*mm, PAGE_W - 2*MARGIN_X - 12*mm)
    pdraw(c, spec['note'], styles['body_small'], MARGIN_X + 6*mm, note_y + 15*mm, PAGE_W - 2*MARGIN_X - 12*mm)
    footer(c)
    c.showPage()


def build_premium_pdf(dest: Path):
    c = canvas.Canvas(str(dest), pagesize=A4)
    c.setTitle('PearlZone premium itinerary - Budapest in 3 days with a 2-day extension')
    # cover
    cover_img = crop_cover(PUBLIC / 'hero.jpg')
    cover_path = ROOT / 'scripts' / '_cover_temp.jpg'
    cover_img.save(cover_path, quality=92)
    c.drawImage(str(cover_path), 0, 0, width=PAGE_W, height=PAGE_H)
    pdraw(c, 'PearlZone premium itinerary', styles['cover_eyebrow'], MARGIN_X, PAGE_H - 44*mm, PAGE_W - 2*MARGIN_X)
    pdraw(c, 'Budapest in 3 days<br/>with a clean 2-day<br/>extension', styles['cover_title'], MARGIN_X, PAGE_H - 68*mm, 116*mm)
    pdraw(c, 'A phone-friendly route plan with local food anchors, official ticket resources, neighborhood notes, and rainy-day backups.', styles['cover_body'], MARGIN_X, PAGE_H - 118*mm, 130*mm)
    x = MARGIN_X
    y = PAGE_H - 146*mm
    for label in ['3-day core', '2 bonus days', 'Offline-friendly', 'Official links included']:
        x += chip(c, x, y, label) + 6
    round_box(c, MARGIN_X, 24*mm, PAGE_W - 2*MARGIN_X, 58*mm, fill=Color(1,1,1, alpha=0.92), stroke=WHITE, radius=18)
    pdraw(c, 'Inside this premium file', styles['section_title'], MARGIN_X + 8*mm, 74*mm, PAGE_W - 2*MARGIN_X - 16*mm)
    cols = [
        ('Day-by-day route logic', 'No guesswork about what pairs well or what to do first.'),
        ('Official resources', 'Visitor pages for transport, baths, Parliament, and more.'),
        ('Food + area notes', 'Breaks and neighborhood context, not just a pile of landmarks.'),
    ]
    col_w = (PAGE_W - 2*MARGIN_X - 16*mm - 12) / 3
    for i, (title, body) in enumerate(cols):
        x0 = MARGIN_X + 8*mm + i * (col_w + 6)
        round_box(c, x0, 28*mm, col_w, 24*mm, fill=HexColor('#E8EEF9'), stroke=HexColor('#E8EEF9'), radius=14)
        pdraw(c, title, styles['card_title'], x0 + 4*mm, 54*mm, col_w - 8*mm)
        pdraw(c, body, styles['body_small'], x0 + 4*mm, 41*mm, col_w - 8*mm)
    c.setFillColor(WHITE)
    c.setFont('Helvetica', 10)
    tag = 'Premium file for Gumroad upload'
    c.drawRightString(PAGE_W - MARGIN_X, 18*mm, tag)
    c.showPage()

    # quick-start page
    c.setFillColor(CREAM)
    c.rect(0,0,PAGE_W,PAGE_H, fill=1, stroke=0)
    header_bar(c, 2)
    top = PAGE_H - TOP_BAR_H - 16*mm
    pdraw(c, 'How to use this guide', styles['page_title'], MARGIN_X, top, PAGE_W - 2*MARGIN_X)
    pdraw(c, 'One page to decide how to use the next five.', styles['page_sub'], MARGIN_X, top - 18*mm, PAGE_W - 2*MARGIN_X)
    pdraw(c, 'The cleanest trip is usually the one where you keep your fixed bookings limited, protect one bath or café reset, and leave one dinner slot flexible.', styles['body'], MARGIN_X, top - 32*mm, PAGE_W - 2*MARGIN_X)
    # planner box
    round_box(c, MARGIN_X, PAGE_H - 145*mm, PAGE_W - 2*MARGIN_X, 56*mm, fill=WHITE, stroke=BORDER, radius=16)
    pdraw(c, 'Quick planning matrix', styles['section_title'], MARGIN_X + 6*mm, PAGE_H - 100*mm, PAGE_W - 2*MARGIN_X - 12*mm)
    matrix = [
        ('Best for first-time visitors', 'Days 1-3 only if you want the essential Budapest shape without extra travel.'),
        ('Best for slower travellers', 'Take Day 4 or Day 5, not both, if you prefer a wider margin and more café time.'),
        ('Reserve-first anchors', 'Parliament, baths, and any dinner that would disappoint you to miss.'),
        ('Open blocks to preserve', 'One bath block, one final-night dinner slot, one rainy-day swap.'),
    ]
    colw = (PAGE_W - 2*MARGIN_X - 18) / 2
    for i, (title, body) in enumerate(matrix):
        r = i // 2
        col = i % 2
        x0 = MARGIN_X + col * (colw + 18)
        y0 = PAGE_H - 116*mm - r * 28*mm
        pdraw(c, title, styles['card_title'], x0 + 5*mm, y0, colw - 10*mm)
        pdraw(c, body, styles['body_small'], x0 + 5*mm, y0 - 8*mm, colw - 10*mm)
    # three callouts
    thirds = (PAGE_W - 2*MARGIN_X - 18) / 3
    items = [
        ('Transport rhythm', 'Use BudapestGO if you plan to ride often. Keep airport transfer, Parliament, and bath tickets together in one notes folder.'),
        ('Food strategy', 'Pick one stronger dinner booking each day and let breakfast / coffee stay flexible. Budapest is better with intentional breaks.'),
        ('Rainy-day logic', 'Swap a river walk for a bath block, House of Music Hungary, House of Terror, or a longer market lunch.'),
    ]
    base_y = 88*mm
    for i, (title, body) in enumerate(items):
        x0 = MARGIN_X + i*(thirds+9)
        round_box(c, x0, base_y, thirds, 46*mm, fill=HexColor('#EEF4FB'), stroke=BORDER, radius=16)
        pdraw(c, title, styles['card_title'], x0+5*mm, base_y+40*mm, thirds-10*mm)
        pdraw(c, body, styles['body_small'], x0+5*mm, base_y+31*mm, thirds-10*mm)
    footer(c)
    c.showPage()

    for idx, spec in enumerate(premium_days, start=3):
        draw_timeline_page(c, idx, spec)

    # food + notes page
    c.setFillColor(CREAM)
    c.rect(0,0,PAGE_W,PAGE_H, fill=1, stroke=0)
    header_bar(c, 8)
    top = PAGE_H - TOP_BAR_H - 16*mm
    pdraw(c, 'Food, coffee, and neighborhood notes', styles['page_title'], MARGIN_X, top, PAGE_W - 2*MARGIN_X)
    pdraw(c, 'Use these to smooth the trip, not to force more bookings.', styles['page_sub'], MARGIN_X, top - 18*mm, PAGE_W - 2*MARGIN_X)
    y = top - 44*mm
    for title, bullets in food_lists:
        round_box(c, MARGIN_X, y - 32*mm, PAGE_W - 2*MARGIN_X, 32*mm, fill=WHITE, stroke=BORDER, radius=16)
        pdraw(c, title, styles['card_title'], MARGIN_X + 6*mm, y - 4*mm, PAGE_W - 2*MARGIN_X - 12*mm)
        bullet_y = y - 11*mm
        for b in bullets:
            pdraw(c, f'• {b}', styles['body_small'], MARGIN_X + 6*mm, bullet_y, PAGE_W - 2*MARGIN_X - 12*mm)
            bullet_y -= 7.5*mm
        y -= 42*mm
    footer(c)
    c.showPage()

    # official links page
    c.setFillColor(CREAM)
    c.rect(0,0,PAGE_W,PAGE_H, fill=1, stroke=0)
    header_bar(c, 9)
    top = PAGE_H - TOP_BAR_H - 16*mm
    pdraw(c, 'Official links to verify before you go', styles['page_title'], MARGIN_X, top, PAGE_W - 2*MARGIN_X)
    pdraw(c, 'A current-minded appendix for travelers', styles['page_sub'], MARGIN_X, top - 18*mm, PAGE_W - 2*MARGIN_X)
    pdraw(c, 'A few details can change. These are the links worth checking before the trip.', styles['body'], MARGIN_X, top - 30*mm, PAGE_W - 2*MARGIN_X)
    y = top - 50*mm
    box_h = 25*mm
    for title, desc, url in official_links:
        round_box(c, MARGIN_X, y - box_h, PAGE_W - 2*MARGIN_X, box_h, fill=WHITE, stroke=BORDER, radius=18)
        pdraw(c, title, styles['card_title'], MARGIN_X + 6*mm, y - 4*mm, 70*mm)
        pdraw(c, desc, styles['body_small'], MARGIN_X + 6*mm, y - 14*mm, 82*mm)
        pdraw(c, url, ParagraphStyle('link', parent=styles['body_small'], textColor=BLUE), MARGIN_X + 95*mm, y - 8*mm, 75*mm)
        y -= (box_h + 4*mm)
    round_box(c, MARGIN_X, 28*mm, PAGE_W - 2*MARGIN_X, 28*mm, fill=SOFT_GOLD, stroke=GOLD, radius=16)
    pdraw(c, 'Final reminder', styles['card_title'], MARGIN_X + 6*mm, 50*mm, PAGE_W - 2*MARGIN_X - 12*mm)
    pdraw(c, 'A great Budapest trip usually comes from better sequencing, not from adding more stops. Use this PDF to remove decisions, not to create a tighter race.', styles['body_small'], MARGIN_X + 6*mm, 40*mm, PAGE_W - 2*MARGIN_X - 12*mm)
    footer(c)
    c.save()
    if cover_path.exists():
        cover_path.unlink()


def draw_check_row(c, x, y, text, col_width):
    c.setStrokeColor(BORDER)
    c.setFillColor(WHITE)
    c.rect(x, y-3, 10, 10, fill=0, stroke=1)
    pdraw(c, text, styles['body'], x + 16, y + 8, col_width - 16)


def build_checklist_pdf(dest: Path):
    c = canvas.Canvas(str(dest), pagesize=A4)
    c.setTitle('PearlZone free Budapest packing checklist')
    for page_idx in range(2):
        c.setFillColor(CREAM)
        c.rect(0,0,PAGE_W,PAGE_H, fill=1, stroke=0)
        header_bar(c, page_idx+1)
        top = PAGE_H - TOP_BAR_H - 16*mm
        if page_idx == 0:
            pdraw(c, 'Free Budapest packing checklist', styles['page_title'], MARGIN_X, top, PAGE_W - 2*MARGIN_X)
            pdraw(c, 'A quick, genuinely useful companion PDF', styles['page_sub'], MARGIN_X, top - 18*mm, PAGE_W - 2*MARGIN_X)
            pdraw(c, 'Use this with the premium itinerary or on its own. It keeps the practical stuff from living in a messy notes app the night before the flight.', styles['body'], MARGIN_X, top - 32*mm, PAGE_W - 2*MARGIN_X)
            round_box(c, MARGIN_X, PAGE_H - 136*mm, PAGE_W - 2*MARGIN_X, 52*mm, fill=HexColor('#E8EDF4'), stroke=BORDER, radius=16)
            pdraw(c, 'Before you fly', styles['card_title'], MARGIN_X + 6*mm, PAGE_H - 88*mm, PAGE_W - 2*MARGIN_X - 12*mm)
            yy = PAGE_H - 100*mm
            for tip in checklist_sections[0][1]:
                pdraw(c, f'• {tip}', styles['body_small'], MARGIN_X + 6*mm, yy, PAGE_W - 2*MARGIN_X - 12*mm)
                yy -= 9*mm
            pdraw(c, 'Carry-on and daily bag essentials', styles['section_title'], MARGIN_X, 138*mm, PAGE_W - 2*MARGIN_X)
            left = checklist_sections[1][1][:3]
            right = checklist_sections[1][1][3:]
            y = 126*mm
            for item in left:
                draw_check_row(c, MARGIN_X, y, item, 78*mm)
                y -= 12*mm
            y = 126*mm
            for item in right:
                draw_check_row(c, MARGIN_X + 85*mm, y, item, 76*mm)
                y -= 12*mm
        else:
            pdraw(c, 'Use-the-city checklist', styles['page_title'], MARGIN_X, top, PAGE_W - 2*MARGIN_X)
            pdraw(c, 'Simple habits that prevent avoidable friction.', styles['page_sub'], MARGIN_X, top - 18*mm, PAGE_W - 2*MARGIN_X)
            y = top - 36*mm
            for title, bullets in checklist_sections[2:]:
                round_box(c, MARGIN_X, y - 44*mm, PAGE_W - 2*MARGIN_X, 44*mm, fill=WHITE, stroke=BORDER, radius=16)
                pdraw(c, title, styles['card_title'], MARGIN_X + 6*mm, y - 4*mm, PAGE_W - 2*MARGIN_X - 12*mm)
                yy = y - 12*mm
                for b in bullets:
                    pdraw(c, f'• {b}', styles['body_small'], MARGIN_X + 6*mm, yy, PAGE_W - 2*MARGIN_X - 12*mm)
                    yy -= 7.2*mm
                y -= 54*mm
            round_box(c, MARGIN_X, 36*mm, PAGE_W - 2*MARGIN_X, 22*mm, fill=SOFT_GOLD, stroke=GOLD, radius=14)
            pdraw(c, 'Tip: if you only remember one thing, keep the first morning and the final evening under-planned. Budapest rewards margin.', styles['body_small'], MARGIN_X + 5*mm, 49*mm, PAGE_W - 2*MARGIN_X - 10*mm)
        footer(c)
        c.showPage()
    c.save()


def main():
    PRODUCT.mkdir(exist_ok=True)
    (PUBLIC / 'downloads').mkdir(parents=True, exist_ok=True)
    premium_pdf = PRODUCT / 'budapest-premium-itinerary.pdf'
    checklist_pdf = PUBLIC / 'downloads' / 'budapest-packing-checklist.pdf'
    build_premium_pdf(premium_pdf)
    build_checklist_pdf(checklist_pdf)
    print('Generated', premium_pdf)
    print('Generated', checklist_pdf)

if __name__ == '__main__':
    main()
