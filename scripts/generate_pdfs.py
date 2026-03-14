from __future__ import annotations

from pathlib import Path
from typing import Iterable

import fitz
from PIL import Image, ImageEnhance
from reportlab.lib.colors import Color, HexColor
from reportlab.lib.enums import TA_CENTER, TA_LEFT
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.units import mm
from reportlab.lib.utils import ImageReader
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.pdfgen import canvas
from reportlab.platypus import Paragraph

ROOT = Path(__file__).resolve().parents[1]
PUBLIC = ROOT / 'public'
PRODUCT = ROOT / 'product-files'
PREVIEW_PREMIUM = PUBLIC / 'previews' / 'premium'
PREVIEW_CHECKLIST = PUBLIC / 'previews' / 'checklist'
DOWNLOADS = PUBLIC / 'downloads'

PAGE_W, PAGE_H = A4
MARGIN_X = 18 * mm
MARGIN_Y = 18 * mm
CONTENT_W = PAGE_W - 2 * MARGIN_X
TOP_BAR_H = 15 * mm

NAVY = HexColor('#0B1531')
BLUE = HexColor('#0B6AFF')
BLUE_SOFT = HexColor('#EAF2FF')
GOLD = HexColor('#F8C13B')
GOLD_SOFT = HexColor('#F6ECD0')
CREAM = HexColor('#F7F3EC')
PAPER = HexColor('#FFFDF8')
TEXT = HexColor('#111827')
MUTED = HexColor('#55657E')
BORDER = HexColor('#DCE5EF')
MIST = HexColor('#EEF4FA')
SLATE = HexColor('#DBE7F2')
WHITE = HexColor('#FFFFFF')

FONT_REG = 'Helvetica'
FONT_MED = 'Helvetica'
FONT_SEM = 'Helvetica-Bold'
FONT_BOLD = 'Helvetica-Bold'


def register_fonts() -> None:
    global FONT_REG, FONT_MED, FONT_SEM, FONT_BOLD
    candidates = {
        'LiberationSans-Regular': Path('/usr/share/fonts/truetype/liberation/LiberationSans-Regular.ttf'),
        'LiberationSans-Bold': Path('/usr/share/fonts/truetype/liberation/LiberationSans-Bold.ttf'),
    }
    for name, path in candidates.items():
        if path.exists():
            pdfmetrics.registerFont(TTFont(name, str(path)))
    if all(path.exists() for path in candidates.values()):
        FONT_REG = 'LiberationSans-Regular'
        FONT_MED = 'LiberationSans-Regular'
        FONT_SEM = 'LiberationSans-Bold'
        FONT_BOLD = 'LiberationSans-Bold'



register_fonts()

styles = {
    'eyebrow': ParagraphStyle(
        'eyebrow',
        fontName=FONT_SEM,
        fontSize=9,
        leading=11,
        textColor=BLUE,
        alignment=TA_LEFT,
    ),
    'cover_small': ParagraphStyle(
        'cover_small',
        fontName=FONT_SEM,
        fontSize=11,
        leading=13,
        textColor=WHITE,
    ),
    'cover_title': ParagraphStyle(
        'cover_title',
        fontName=FONT_BOLD,
        fontSize=29,
        leading=34,
        textColor=WHITE,
    ),
    'cover_body': ParagraphStyle(
        'cover_body',
        fontName=FONT_REG,
        fontSize=12,
        leading=17,
        textColor=WHITE,
    ),
    'page_title': ParagraphStyle(
        'page_title',
        fontName=FONT_BOLD,
        fontSize=24,
        leading=29,
        textColor=TEXT,
    ),
    'page_sub': ParagraphStyle(
        'page_sub',
        fontName=FONT_REG,
        fontSize=12,
        leading=16,
        textColor=MUTED,
    ),
    'section': ParagraphStyle(
        'section',
        fontName=FONT_SEM,
        fontSize=13,
        leading=15,
        textColor=TEXT,
    ),
    'body': ParagraphStyle(
        'body',
        fontName=FONT_REG,
        fontSize=10.8,
        leading=15,
        textColor=MUTED,
    ),
    'body_small': ParagraphStyle(
        'body_small',
        fontName=FONT_REG,
        fontSize=9.5,
        leading=12.5,
        textColor=MUTED,
    ),
    'card_title': ParagraphStyle(
        'card_title',
        fontName=FONT_BOLD,
        fontSize=12.5,
        leading=15,
        textColor=TEXT,
    ),
    'card_body': ParagraphStyle(
        'card_body',
        fontName=FONT_REG,
        fontSize=9.6,
        leading=12.8,
        textColor=MUTED,
    ),
    'button': ParagraphStyle(
        'button',
        fontName=FONT_SEM,
        fontSize=9.5,
        leading=11,
        textColor=WHITE,
        alignment=TA_CENTER,
    ),
    'footer': ParagraphStyle(
        'footer',
        fontName=FONT_REG,
        fontSize=8.8,
        leading=10.2,
        textColor=MUTED,
    ),
}

premium_days = [
    {
        'title': 'Day 1 - Castle District and Danube',
        'subtitle': 'The strong first-impression day',
        'intro': 'Open with Budapest at its most cinematic, but do it in an order that still feels elegant once you are walking it.',
        'book_first': 'Reserve Matthias Church or any tower ticket only if those interiors matter to you. Leave the riverfront flexible for sunset.',
        'meal_anchor': 'Keep lunch inside the Castle area so the midday transition stays short and calm.',
        'swap': 'If the weather is poor, shorten the lookout time and lean into the church, a longer lunch, and the evening river stretch.',
        'steps': [
            ('08:00', 'Fisherman\'s Bastion and Trinity Square', 'Go early while the terraces still feel calm and the views are clear.'),
            ('09:15', 'Matthias Church interior', 'If the interior is a priority, treat this as the morning\'s only fixed ticketed anchor.'),
            ('10:45', 'Castle courtyards and walls', 'Walk the courtyards slowly instead of trying to turn this block into a museum sprint.'),
            ('12:30', 'Castle lunch break', 'Use lunch as a real pause before you descend to the river rather than another stop.'),
            ('16:30', 'Chain Bridge side and Danube finish', 'Let the evening lead. Cruise if you want it; otherwise keep the riverfront open for sunset and dinner.'),
        ],
    },
    {
        'title': 'Day 2 - Parliament, baths, and the Quarter',
        'subtitle': 'Formal Budapest, then full recovery mode',
        'intro': 'This day works because the structure loosens after lunch: one clear reservation in the morning, one long bath block, then dinner and evening energy later on.',
        'book_first': 'If Parliament matters, book that first. Choose your bath slot next. Those are the only decisions that really need to be locked early.',
        'meal_anchor': 'Lunch around the Basilica or Hold utca works well between Parliament and the baths.',
        'swap': 'If you skip the baths, use the afternoon for the Basilica, a longer café stop, and a softer walk into the Jewish Quarter.',
        'steps': [
            ('08:30', 'Parliament riverfront arrival', 'Keep the morning precise and let your Parliament booking set the pace for the first block.'),
            ('10:30', 'Shoes memorial and Pest-side walk', 'Stay on the Pest side and let the river walk bridge the formal morning and the looser rest of the day.'),
            ('12:15', 'Lunch and reset', 'Eat before the baths so the afternoon can genuinely slow down.'),
            ('14:30', 'Széchenyi, Gellért, Rudas, or Lukács', 'Give the bath a proper block. Budapest thermal culture works best when you stop treating it like a quick add-on.'),
            ('19:00', 'Jewish Quarter dinner and drinks', 'Choose one strong dinner, then let the evening become as social or as quiet as you want.'),
        ],
    },
    {
        'title': 'Day 3 - City Park and Andrássy Avenue',
        'subtitle': 'A more breathable final core day',
        'intro': 'Day three should feel lighter on your feet. You still get architecture, culture, and a good last dinner, but with more room for cafés and recovery.',
        'book_first': 'Only reserve House of Music, House of Terror, or Opera if one of them is a must for your trip.',
        'meal_anchor': 'A slower lunch or pastry stop between City Park and Andrássy is what makes this day land well.',
        'swap': 'If it rains, move the outdoor park time into one indoor anchor and keep Andrássy as a clean transit corridor.',
        'steps': [
            ('09:00', 'Heroes\' Square and City Park entry', 'Start where the grand urban frame still feels calm and you are not yet competing with heavy midday crowds.'),
            ('10:15', 'Choose one main park anchor', 'House of Music, Vajdahunyad, a bath return, or simply the park itself. One clear choice always beats three partial ones.'),
            ('13:00', 'Lunch or café reset', 'Use the transition out of the park for a longer break instead of forcing another sight immediately.'),
            ('15:00', 'Andrássy descent', 'Walk or ride the avenue back into the city centre at an easy pace with room for design shops and coffee.'),
            ('19:00', 'Final dinner booking', 'This is the night to spend slightly more and finish the 3-day core with a memorable table.'),
        ],
    },
    {
        'title': 'Day 4 - Szentendre add-on',
        'subtitle': 'A slower art-town extension',
        'intro': 'Use Szentendre when you want a day that feels lighter, smaller in scale, and more relaxed than another dense Budapest route.',
        'book_first': 'You do not need to over-plan this extension. The value is in the slower pace, not in a heavy list of museums.',
        'meal_anchor': 'A long lunch in the centre or near the river is enough to make the town feel worth the detour.',
        'swap': 'If you wake up and want to stay in Budapest, skip Szentendre without guilt and give yourself a slower city day instead.',
        'steps': [
            ('09:00', 'H5 departure', 'Go in the morning so the town still feels quiet when you arrive.'),
            ('10:00', 'Old town wander', 'Let the side streets, church corners, and small squares set the pace instead of chasing every museum.'),
            ('12:30', 'Long lunch', 'Use lunch as the centre of the day rather than something you squeeze between stops.'),
            ('15:00', 'Optional gallery or river stretch', 'Pick one more thing based on the weather and your mood.'),
            ('18:00', 'Return to Budapest', 'Come back while the evening still feels open and the detour still feels restorative.'),
        ],
    },
    {
        'title': 'Day 5 - Great Synagogue and a food-led finish',
        'subtitle': 'A softer final day in the Quarter',
        'intro': 'This closing day is less monumental and more lived-in: a cultural anchor in the morning, food and design in the afternoon, and atmosphere after dark.',
        'book_first': 'If the Great Synagogue matters to you, check the official visitor flow before the day starts. Leave the rest of the day intentionally open.',
        'meal_anchor': 'Keep lunch casual and flavour-led: market hall, courtyard dining, or a modern Hungarian spot all work well here.',
        'swap': 'If you are tired, turn this day into coffee, light shopping, one cultural stop, and an earlier dinner.',
        'steps': [
            ('10:00', 'Great Synagogue and the surrounding streets', 'Let the synagogue area give the day its centre of gravity and emotional tone.'),
            ('12:15', 'Lunch in or near the Quarter', 'This is a good block for something lively and relaxed rather than overly formal.'),
            ('14:30', 'Design shops and coffee loop', 'Use the afternoon for browsing, a longer coffee, and whatever final purchases actually matter.'),
            ('17:30', 'Golden-hour neighborhood walk', 'The streets themselves become the main attraction here.'),
            ('20:00', 'Final-night choice', 'Go elegant, casual, or social - but make it deliberate rather than default.'),
        ],
    },
]

neighborhood_cards = [
    (
        'Castle District',
        'Best used for a strong first morning, a slower lunch, and a photo-led walk rather than too many museum interiors at once.',
        'Morning light, panoramic views, quiet courtyards, and a natural first-day sense of occasion.',
    ),
    (
        'Parliament and Basilica zone',
        'Ideal for the formal city core, one coffee stop, and a cleaner transition into lunch before the baths.',
        'Use this area for the most time-sensitive ticket on the trip, not for a day full of extra detours.',
    ),
    (
        'Jewish Quarter',
        'Where the route wants to go after dark. It carries the evening energy best and gives you the easiest dinner options.',
        'Choose one strong dinner, then add bars only if the night still feels fresh.',
    ),
    (
        'City Park and Andrássy',
        'A better fit for your lightest day: culture, architecture, and coffee without turning the route into another race.',
        'Use one main indoor anchor here and let the avenue do the rest of the work.',
    ),
]

bath_cards = [
    ('Széchenyi', 'The grand outdoor classic', 'Best if you want the iconic Budapest bath experience and do not mind a busier atmosphere.'),
    ('Gellért', 'Art Nouveau and calmer interiors', 'A stronger fit if architecture and indoor mood matter more than outdoor social energy.'),
    ('Rudas', 'Historic pools and river-view rooftop', 'The choice for a more distinctive mood, especially if you want a slightly more atmospheric bath block.'),
    ('Lukács', 'Lower-key and more local-feeling', 'A good option if you want the bath day to feel simpler, less theatrical, and easier on the senses.'),
]

reserve_cards = [
    ('Reserve first', 'Parliament, your chosen bath if you want a timed entry, and any dinner that would actually disappoint you to miss.'),
    ('Keep flexible', 'Castle weather, coffee stops, the Szentendre decision, and your final-night dinner if you want more spontaneity.'),
    ('Save offline', 'BudapestGO, the airport transfer plan, accommodation address, and the PDFs themselves.'),
]

base_cards = [
    ('Stay around District V if you want the cleanest first-time base.', 'Easy transport, easy dinners, and a straightforward feel for a short Budapest trip.'),
    ('Stay around District VII if evening energy matters most.', 'Best if you want stronger nightlife and easy restaurant density around the Jewish Quarter.'),
    ('Stay on the Buda side only if you actively want the quieter mood.', 'Beautiful mornings and great views, but less convenient if you plan to end most nights in Pest.'),
]

official_links = [
    ('BudapestGO', 'Digital tickets, route planning, and Airport Express support.', 'bkk.hu', 'https://bkk.hu/en/tickets-and-passes/budapestgo/'),
    ('Airport Express 100E', 'The direct airport-to-city bus line and its special ticket rules.', 'bkk.hu', 'https://bkk.hu/en/travel-information/airport-express/'),
    ('Parliament visitors', 'Official tour information, opening windows, and ticket guidance.', 'parlament.hu', 'https://www.parlament.hu/web/visitors'),
    ('Széchenyi Bath', 'Opening hours, ticket types, and current bath information.', 'szechenyibath.hu', 'https://www.szechenyibath.hu/'),
    ('Matthias Church', 'Current access, tickets, and visitor rules in the Castle District.', 'matyas-templom.hu', 'https://matyas-templom.hu/en/'),
    ('Great Synagogue', 'Official visitor information for the Dohány Street Synagogue.', 'dohany-zsinagoga.hu', 'https://dohany-zsinagoga.hu/'),
    ('Central Market Hall', 'Opening hours, directions, and market information.', 'piaconline.hu', 'https://piaconline.hu/en/central-market-hall/'),
    ('House of Music Hungary', 'Exhibitions, current programmes, and ticketing.', 'magyarzenehaza.com', 'https://magyarzenehaza.com/en/'),
]

checklist_before_fly = [
    'Save your accommodation address offline and keep one screenshot of the route from the airport.',
    'Download BudapestGO before you leave if you plan to use public transport often.',
    'Book the small number of time-sensitive highlights that actually matter to you.',
    'Screenshot your first dinner reservation and the next morning\'s first anchor.',
]

arrival_first_hours = [
    'Use the airport ride to set up what you need for day one: PDF saved, phone charged, and transport sorted.',
    'If you are arriving late, keep the first evening small. A calm dinner beats trying to start sightseeing half-tired.',
    'For an early arrival, get bags dropped, walk the river once, and then stop. Budapest rewards a gentler first landing.',
]

packing_groups = [
    (
        'Documents and money',
        [
            'Passport or ID',
            'Primary payment card',
            'Backup payment option or small emergency cash',
            'Offline confirmation for accommodation',
        ],
    ),
    (
        'Tech and power',
        [
            'Phone charger and cable',
            'Compact power bank',
            'The adapter you actually need',
            'Offline copy of the PDFs and ticket confirmations',
        ],
    ),
    (
        'Walking day kit',
        [
            'Comfortable shoes',
            'Reusable water bottle',
            'Compact umbrella or light layer',
            'Tissues and a small cross-body bag',
        ],
    ),
    (
        'Bath bag add-ons',
        [
            'Swimsuit',
            'Flip-flops',
            'Small towel if your ticket does not include one',
            'Hair tie and a dry pouch for your phone',
        ],
    ),
]

city_habits = [
    'Keep one breakfast and one coffee stop genuinely unhurried every day.',
    'Use the bath day as the recovery day, not as the day to add even more tickets.',
    'If rain hits, switch the route rather than fighting it. A long lunch and one indoor anchor still count as a good Budapest day.',
    'Wear a layer in the evening - the riverfront can feel cooler than the daytime forecast suggests.',
]

departure_reset = [
    'Confirm your airport plan the night before and set the ride buffer generously.',
    'Pack the evening before so the final morning is only shower, coffee, and checkout.',
    'Keep the last meal close to your hotel if you have an early departure the next day.',
    'Leave one last window for pastries or market shopping only if luggage space is already solved.',
]


def pdraw(c: canvas.Canvas, text: str, style: ParagraphStyle, x: float, top_y: float, width: float) -> float:
    para = Paragraph(text, style)
    _, h = para.wrap(width, 10000)
    para.drawOn(c, x, top_y - h)
    return h


def round_box(c: canvas.Canvas, x: float, y: float, w: float, h: float, fill=WHITE, stroke=BORDER, radius=16, line=1) -> None:
    c.setFillColor(fill)
    c.setStrokeColor(stroke)
    c.setLineWidth(line)
    c.roundRect(x, y, w, h, radius, fill=1, stroke=1)


def draw_top_bar(c: canvas.Canvas, page_no: int, total_pages: int, title: str) -> None:
    c.setFillColor(NAVY)
    c.rect(0, PAGE_H - TOP_BAR_H, PAGE_W, TOP_BAR_H, fill=1, stroke=0)
    c.setFillColor(WHITE)
    c.setFont(FONT_BOLD, 11)
    c.drawString(MARGIN_X, PAGE_H - TOP_BAR_H + 5.4 * mm, 'PearlZone')
    c.setFont(FONT_REG, 10)
    c.drawRightString(PAGE_W - MARGIN_X, PAGE_H - TOP_BAR_H + 5.5 * mm, f'{title}  -  page {page_no} / {total_pages}')


def draw_footer(c: canvas.Canvas, right_note: str = 'Save the PDF offline before you fly.') -> None:
    y = 14 * mm
    c.setStrokeColor(BORDER)
    c.setLineWidth(1)
    c.line(MARGIN_X, y + 7 * mm, PAGE_W - MARGIN_X, y + 7 * mm)
    c.setFillColor(MUTED)
    c.setFont(FONT_REG, 9)
    c.drawString(MARGIN_X, y, 'pearlzone.hu')
    c.drawRightString(PAGE_W - MARGIN_X, y, right_note)


def draw_chip(c: canvas.Canvas, x: float, y: float, label: str, fill: Color = Color(1, 1, 1, alpha=0.12), stroke: Color = Color(1, 1, 1, alpha=0.32), text_color: Color = WHITE) -> float:
    w = 11 * mm + pdfmetrics.stringWidth(label, FONT_SEM, 10)
    round_box(c, x, y, w, 10 * mm, fill=fill, stroke=stroke, radius=14, line=0.8)
    c.setFillColor(text_color)
    c.setFont(FONT_SEM, 10)
    c.drawCentredString(x + w / 2, y + 3.4 * mm, label)
    return w


def draw_text_button(c: canvas.Canvas, x: float, y: float, w: float, h: float, label: str, url: str, fill=BLUE, text_color=WHITE, stroke=BLUE) -> None:
    round_box(c, x, y, w, h, fill=fill, stroke=stroke, radius=13, line=0)
    c.setFillColor(text_color)
    c.setFont(FONT_SEM, 9.3)
    c.drawCentredString(x + w / 2, y + 4.4 * mm, label)
    c.linkURL(url, (x, y, x + w, y + h), relative=0, thickness=0)


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
    img = Image.blend(img, overlay, 0.35)
    img = ImageEnhance.Contrast(img).enhance(1.06)
    img = ImageEnhance.Color(img).enhance(0.96)
    return img


def draw_cover(c: canvas.Canvas, hero_path: Path) -> None:
    cover = crop_cover(hero_path)
    temp = ROOT / '.tmp-cover.jpg'
    cover.save(temp, quality=94)
    c.drawImage(ImageReader(str(temp)), 0, 0, width=PAGE_W, height=PAGE_H)
    c.setFillColor(Color(1, 1, 1, alpha=0.88))
    c.setFont(FONT_SEM, 12)
    c.drawString(MARGIN_X, PAGE_H - 42 * mm, 'PearlZone premium itinerary')
    pdraw(c, 'Budapest in 3 days with a polished 2-day extension', styles['cover_title'], MARGIN_X, PAGE_H - 60 * mm, 120 * mm)
    pdraw(c, 'A calm city guide for first-time visitors who want strong structure, easy pacing, and the small practical touches that make the trip feel premium.', styles['cover_body'], MARGIN_X, PAGE_H - 108 * mm, 138 * mm)

    chip_y = PAGE_H - 141 * mm
    x = MARGIN_X
    for chip in ['3 core days', '2 add-on days', 'Offline-friendly', 'Official links included']:
        x += draw_chip(c, x, chip_y, chip) + 3.4 * mm

    panel_x = MARGIN_X
    panel_y = 20 * mm
    panel_h = 49 * mm
    round_box(c, panel_x, panel_y, CONTENT_W, panel_h, fill=Color(1, 1, 1, alpha=0.94), stroke=Color(1, 1, 1, alpha=0.2), radius=20, line=0.8)
    pdraw(c, 'Inside the guide', ParagraphStyle('inside', fontName=FONT_BOLD, fontSize=13.5, leading=16, textColor=TEXT), panel_x + 7 * mm, panel_y + panel_h - 8 * mm, 80 * mm)
    features = [
        ('Day-by-day pacing', 'A cleaner sequence for the city\'s biggest sights.'),
        ('Reserve-first notes', 'What is worth booking early and what can wait.'),
        ('Links appendix', 'Current visitor pages collected in one place.'),
    ]
    inner_x = panel_x + 7 * mm
    card_w = (CONTENT_W - 14 * mm - 8 * mm) / 3
    for i, (title, body) in enumerate(features):
        card_x = inner_x + i * (card_w + 4 * mm)
        round_box(c, card_x, panel_y + 6 * mm, card_w, 22 * mm, fill=BLUE_SOFT, stroke=BLUE_SOFT, radius=14, line=0)
        pdraw(c, title, styles['card_title'], card_x + 4 * mm, panel_y + 22 * mm, card_w - 8 * mm)
        pdraw(c, body, styles['card_body'], card_x + 4 * mm, panel_y + 12 * mm, card_w - 8 * mm)

    c.setFillColor(WHITE)
    c.setFont(FONT_REG, 10)
    c.drawRightString(PAGE_W - MARGIN_X, 13 * mm, 'Premium PDF')
    c.showPage()
    temp.unlink(missing_ok=True)


def draw_info_card(c: canvas.Canvas, x: float, y: float, w: float, title: str, body: str, fill=WHITE, stroke=BORDER, accent=BLUE) -> float:
    h = 28 * mm
    round_box(c, x, y, w, h, fill=fill, stroke=stroke, radius=16, line=1)
    c.setFillColor(accent)
    c.circle(x + 5 * mm, y + h - 7 * mm, 1.8 * mm, fill=1, stroke=0)
    pdraw(c, title, styles['card_title'], x + 9 * mm, y + h - 4.5 * mm, w - 14 * mm)
    pdraw(c, body, styles['card_body'], x + 5 * mm, y + h - 13.5 * mm, w - 10 * mm)
    return h


def draw_planning_page(c: canvas.Canvas, page_no: int, total_pages: int) -> None:
    c.setFillColor(CREAM)
    c.rect(0, 0, PAGE_W, PAGE_H, fill=1, stroke=0)
    draw_top_bar(c, page_no, total_pages, 'Budapest itinerary')
    top = PAGE_H - TOP_BAR_H - 12 * mm
    pdraw(c, 'How to use this guide', styles['page_title'], MARGIN_X, top, CONTENT_W)
    pdraw(c, 'A fast setup page for the decisions that matter before you go.', styles['page_sub'], MARGIN_X, top - 16 * mm, CONTENT_W)

    col_gap = 5 * mm
    card_w = (CONTENT_W - 2 * col_gap) / 3
    y = top - 52 * mm
    for i, (title, body) in enumerate(reserve_cards):
        draw_info_card(c, MARGIN_X + i * (card_w + col_gap), y, card_w, title, body, fill=WHITE, stroke=BORDER)

    box_y = y - 53 * mm
    round_box(c, MARGIN_X, box_y, CONTENT_W, 60 * mm, fill=WHITE, stroke=BORDER, radius=18)
    pdraw(c, 'Choose the base that matches the trip you want', styles['section'], MARGIN_X + 6 * mm, box_y + 53 * mm, CONTENT_W - 12 * mm)
    base_w = (CONTENT_W - 12 * mm - 8 * mm) / 3
    for i, (title, body) in enumerate(base_cards):
        x = MARGIN_X + 6 * mm + i * (base_w + 4 * mm)
        round_box(c, x, box_y + 9 * mm, base_w, 33 * mm, fill=MIST, stroke=MIST, radius=15, line=0)
        pdraw(c, title, styles['card_title'], x + 4 * mm, box_y + 37 * mm, base_w - 8 * mm)
        pdraw(c, body, styles['card_body'], x + 4 * mm, box_y + 27 * mm, base_w - 8 * mm)

    note_y = 34 * mm
    round_box(c, MARGIN_X, note_y, CONTENT_W, 22 * mm, fill=GOLD_SOFT, stroke=GOLD, radius=14)
    pdraw(c, 'Best general rule: build around one timed highlight, one proper meal, and one real recovery block each day. Budapest gets better when the schedule breathes.', styles['body_small'], MARGIN_X + 5 * mm, note_y + 15 * mm, CONTENT_W - 10 * mm)
    draw_footer(c)
    c.showPage()


def draw_day_page(c: canvas.Canvas, page_no: int, total_pages: int, day: dict[str, object]) -> None:
    c.setFillColor(CREAM)
    c.rect(0, 0, PAGE_W, PAGE_H, fill=1, stroke=0)
    draw_top_bar(c, page_no, total_pages, 'Budapest itinerary')
    top = PAGE_H - TOP_BAR_H - 12 * mm
    title_h = pdraw(c, day['title'], styles['page_title'], MARGIN_X, top, 122 * mm)
    sub_top = top - title_h - 4 * mm
    sub_h = pdraw(c, day['subtitle'], styles['page_sub'], MARGIN_X, sub_top, 122 * mm)
    intro_top = sub_top - sub_h - 8 * mm
    intro_h = pdraw(c, day['intro'], styles['body'], MARGIN_X, intro_top, 122 * mm)

    left_w = 120 * mm
    right_x = MARGIN_X + left_w + 7 * mm
    right_w = PAGE_W - MARGIN_X - right_x

    y = intro_top - intro_h - 10 * mm
    for time, title, body in day['steps']:
        time_x = MARGIN_X
        card_x = MARGIN_X + 24 * mm
        box_h = 24 * mm
        round_box(c, time_x, y - box_h + 1 * mm, 20 * mm, 10 * mm, fill=GOLD_SOFT, stroke=GOLD_SOFT, radius=10, line=0)
        c.setFillColor(TEXT)
        c.setFont(FONT_SEM, 10)
        c.drawCentredString(time_x + 10 * mm, y - box_h + 4.4 * mm, time)
        round_box(c, card_x, y - box_h, left_w - 24 * mm, box_h, fill=WHITE, stroke=BORDER, radius=16)
        pdraw(c, title, styles['card_title'], card_x + 5 * mm, y - 3 * mm, left_w - 34 * mm)
        pdraw(c, body, styles['card_body'], card_x + 5 * mm, y - 11.5 * mm, left_w - 34 * mm)
        y -= 31 * mm

    sidebar_y = top - 3 * mm
    boxes = [
        ('Book first', day['book_first'], WHITE),
        ('Food anchor', day['meal_anchor'], MIST),
        ('If plans change', day['swap'], GOLD_SOFT),
    ]
    for title, body, fill in boxes:
        round_box(c, right_x, sidebar_y - 31 * mm, right_w, 31 * mm, fill=fill, stroke=BORDER, radius=16)
        pdraw(c, title, styles['card_title'], right_x + 4 * mm, sidebar_y - 4 * mm, right_w - 8 * mm)
        pdraw(c, body, styles['card_body'], right_x + 4 * mm, sidebar_y - 12.5 * mm, right_w - 8 * mm)
        sidebar_y -= 37 * mm

    draw_footer(c)
    c.showPage()


def draw_neighborhood_page(c: canvas.Canvas, page_no: int, total_pages: int) -> None:
    c.setFillColor(CREAM)
    c.rect(0, 0, PAGE_W, PAGE_H, fill=1, stroke=0)
    draw_top_bar(c, page_no, total_pages, 'Budapest itinerary')
    top = PAGE_H - TOP_BAR_H - 12 * mm
    pdraw(c, 'Food and neighborhood anchors', styles['page_title'], MARGIN_X, top, CONTENT_W)
    pdraw(c, 'Use these as route-shaping notes, not as another list of places to race through.', styles['page_sub'], MARGIN_X, top - 16 * mm, CONTENT_W)

    y = top - 44 * mm
    card_w = (CONTENT_W - 6 * mm) / 2
    for i, (title, body, note) in enumerate(neighborhood_cards):
        x = MARGIN_X + (i % 2) * (card_w + 6 * mm)
        if i and i % 2 == 0:
            y -= 57 * mm
        round_box(c, x, y - 49 * mm, card_w, 49 * mm, fill=WHITE, stroke=BORDER, radius=18)
        pdraw(c, title, styles['card_title'], x + 5 * mm, y - 5 * mm, card_w - 10 * mm)
        pdraw(c, body, styles['body_small'], x + 5 * mm, y - 15 * mm, card_w - 10 * mm)
        pdraw(c, f'<b>Best used for:</b> {note}', styles['body_small'], x + 5 * mm, y - 34 * mm, card_w - 10 * mm)

    note_y = 32 * mm
    round_box(c, MARGIN_X, note_y, CONTENT_W, 24 * mm, fill=BLUE_SOFT, stroke=BLUE_SOFT, radius=14, line=0)
    pdraw(c, 'A Budapest trip usually feels better when one meal a day is genuinely planned, one coffee stop stays spontaneous, and one evening remains flexible.', styles['body_small'], MARGIN_X + 5 * mm, note_y + 16 * mm, CONTENT_W - 10 * mm)
    draw_footer(c)
    c.showPage()


def draw_baths_page(c: canvas.Canvas, page_no: int, total_pages: int) -> None:
    c.setFillColor(CREAM)
    c.rect(0, 0, PAGE_W, PAGE_H, fill=1, stroke=0)
    draw_top_bar(c, page_no, total_pages, 'Budapest itinerary')
    top = PAGE_H - TOP_BAR_H - 12 * mm
    pdraw(c, 'Bath style guide and easy route edits', styles['page_title'], MARGIN_X, top, CONTENT_W)
    pdraw(c, 'This is where many first-time visitors overcomplicate the trip. Pick one bath, use it properly, and keep the rest of the day lighter.', styles['page_sub'], MARGIN_X, top - 16 * mm, CONTENT_W)

    y = top - 40 * mm
    card_w = (CONTENT_W - 9 * mm) / 2
    for i, (title, kicker, body) in enumerate(bath_cards):
        x = MARGIN_X + (i % 2) * (card_w + 9 * mm)
        if i and i % 2 == 0:
            y -= 46 * mm
        round_box(c, x, y - 39 * mm, card_w, 39 * mm, fill=WHITE, stroke=BORDER, radius=18)
        pdraw(c, title, styles['card_title'], x + 5 * mm, y - 5 * mm, card_w - 10 * mm)
        pdraw(c, kicker, ParagraphStyle('kicker', fontName=FONT_SEM, fontSize=9.4, leading=11, textColor=BLUE), x + 5 * mm, y - 13 * mm, card_w - 10 * mm)
        pdraw(c, body, styles['body_small'], x + 5 * mm, y - 22 * mm, card_w - 10 * mm)

    lower_y = 50 * mm
    round_box(c, MARGIN_X, lower_y, CONTENT_W, 34 * mm, fill=WHITE, stroke=BORDER, radius=18)
    pdraw(c, 'Quick route edits', styles['section'], MARGIN_X + 6 * mm, lower_y + 28 * mm, CONTENT_W - 12 * mm)
    edits = [
        'Only have 2 nights? Keep Days 1 and 2, then fold the strongest part of Day 3 into your final morning.',
        'Rainy day? Swap long outdoor stretches for one indoor anchor and a longer lunch. The trip still works.',
        'Energy drop? Cut one museum, not the meal or bath block. The route should stay pleasant, not merely complete.',
    ]
    yy = lower_y + 19 * mm
    for line in edits:
        pdraw(c, f'• {line}', styles['body_small'], MARGIN_X + 6 * mm, yy, CONTENT_W - 12 * mm)
        yy -= 8 * mm
    draw_footer(c)
    c.showPage()


def draw_links_page(c: canvas.Canvas, page_no: int, total_pages: int) -> None:
    c.setFillColor(CREAM)
    c.rect(0, 0, PAGE_W, PAGE_H, fill=1, stroke=0)
    draw_top_bar(c, page_no, total_pages, 'Budapest itinerary')
    top = PAGE_H - TOP_BAR_H - 12 * mm
    pdraw(c, 'Essential official links', styles['page_title'], MARGIN_X, top, CONTENT_W)
    pdraw(c, 'These are the pages worth checking for the details that move: tickets, access windows, bath information, and a few practical city tools.', styles['page_sub'], MARGIN_X, top - 16 * mm, CONTENT_W)

    y = top - 39 * mm
    card_w = (CONTENT_W - 6 * mm) / 2
    card_h = 33 * mm
    button_w = 26 * mm
    for i, (title, desc, domain, url) in enumerate(official_links):
        x = MARGIN_X + (i % 2) * (card_w + 6 * mm)
        if i and i % 2 == 0:
            y -= card_h + 5 * mm
        round_box(c, x, y - card_h, card_w, card_h, fill=WHITE, stroke=BORDER, radius=16)
        pdraw(c, title, styles['card_title'], x + 5 * mm, y - 4 * mm, card_w - button_w - 14 * mm)
        pdraw(c, desc, styles['card_body'], x + 5 * mm, y - 14 * mm, card_w - button_w - 14 * mm)
        draw_text_button(c, x + card_w - button_w - 5 * mm, y - 18.5 * mm, button_w, 10 * mm, 'Open site', url, fill=BLUE, text_color=WHITE, stroke=BLUE)

    note_y = 20 * mm
    round_box(c, MARGIN_X, note_y, CONTENT_W, 21 * mm, fill=GOLD_SOFT, stroke=GOLD, radius=14)
    pdraw(c, 'Use official pages for time-sensitive details. Use the itinerary for the route logic, pacing, and sequencing decisions that do not need to change every week.', styles['body_small'], MARGIN_X + 5 * mm, note_y + 14 * mm, CONTENT_W - 10 * mm)
    draw_footer(c)
    c.showPage()


def checklist_cover(c: canvas.Canvas, page_no: int, total_pages: int) -> None:
    c.setFillColor(CREAM)
    c.rect(0, 0, PAGE_W, PAGE_H, fill=1, stroke=0)
    draw_top_bar(c, page_no, total_pages, 'Packing checklist')
    top = PAGE_H - TOP_BAR_H - 12 * mm
    pdraw(c, 'Budapest packing checklist', styles['page_title'], MARGIN_X, top, CONTENT_W)
    pdraw(c, 'A short companion PDF for the practical side of the trip.', styles['page_sub'], MARGIN_X, top - 16 * mm, CONTENT_W)

    round_box(c, MARGIN_X, top - 86 * mm, CONTENT_W, 48 * mm, fill=WHITE, stroke=BORDER, radius=18)
    pdraw(c, 'Before you fly', styles['section'], MARGIN_X + 6 * mm, top - 46 * mm, CONTENT_W - 12 * mm)
    yy = top - 56 * mm
    for item in checklist_before_fly:
        pdraw(c, f'• {item}', styles['body_small'], MARGIN_X + 6 * mm, yy, CONTENT_W - 12 * mm)
        yy -= 7.5 * mm

    round_box(c, MARGIN_X, 84 * mm, CONTENT_W, 54 * mm, fill=MIST, stroke=BORDER, radius=18)
    pdraw(c, 'Your first 12 hours in Budapest', styles['section'], MARGIN_X + 6 * mm, 129 * mm, CONTENT_W - 12 * mm)
    yy = 119 * mm
    for item in arrival_first_hours:
        pdraw(c, f'• {item}', styles['body_small'], MARGIN_X + 6 * mm, yy, CONTENT_W - 12 * mm)
        yy -= 10 * mm

    draw_footer(c)
    c.showPage()


def checklist_packing_page(c: canvas.Canvas, page_no: int, total_pages: int) -> None:
    c.setFillColor(CREAM)
    c.rect(0, 0, PAGE_W, PAGE_H, fill=1, stroke=0)
    draw_top_bar(c, page_no, total_pages, 'Packing checklist')
    top = PAGE_H - TOP_BAR_H - 12 * mm
    pdraw(c, 'Packing matrix', styles['page_title'], MARGIN_X, top, CONTENT_W)
    pdraw(c, 'A compact layout for the items that matter most on a Budapest trip.', styles['page_sub'], MARGIN_X, top - 16 * mm, CONTENT_W)

    card_w = (CONTENT_W - 6 * mm) / 2
    y = top - 40 * mm
    for i, (title, items) in enumerate(packing_groups):
        x = MARGIN_X + (i % 2) * (card_w + 6 * mm)
        if i and i % 2 == 0:
            y -= 58 * mm
        round_box(c, x, y - 52 * mm, card_w, 52 * mm, fill=WHITE, stroke=BORDER, radius=18)
        pdraw(c, title, styles['card_title'], x + 5 * mm, y - 4 * mm, card_w - 10 * mm)
        yy = y - 14 * mm
        for item in items:
            c.setStrokeColor(BORDER)
            c.rect(x + 5 * mm, yy - 2.5 * mm, 9, 9, fill=0, stroke=1)
            pdraw(c, item, styles['body_small'], x + 11 * mm, yy + 4 * mm, card_w - 16 * mm)
            yy -= 10 * mm

    draw_footer(c)
    c.showPage()


def checklist_city_page(c: canvas.Canvas, page_no: int, total_pages: int) -> None:
    c.setFillColor(CREAM)
    c.rect(0, 0, PAGE_W, PAGE_H, fill=1, stroke=0)
    draw_top_bar(c, page_no, total_pages, 'Packing checklist')
    top = PAGE_H - TOP_BAR_H - 12 * mm
    pdraw(c, 'On-the-ground reset', styles['page_title'], MARGIN_X, top, CONTENT_W)
    pdraw(c, 'Simple habits that keep the trip feeling calm once you are already there.', styles['page_sub'], MARGIN_X, top - 16 * mm, CONTENT_W)

    first_y = top - 34 * mm
    round_box(c, MARGIN_X, first_y - 46 * mm, CONTENT_W, 46 * mm, fill=WHITE, stroke=BORDER, radius=18)
    pdraw(c, 'Daily habits that keep the route easy', styles['section'], MARGIN_X + 6 * mm, first_y - 4 * mm, CONTENT_W - 12 * mm)
    yy = first_y - 13 * mm
    for item in city_habits:
        pdraw(c, f'• {item}', styles['body_small'], MARGIN_X + 6 * mm, yy, CONTENT_W - 12 * mm)
        yy -= 8 * mm

    second_y = 96 * mm
    round_box(c, MARGIN_X, second_y, CONTENT_W, 44 * mm, fill=MIST, stroke=BORDER, radius=18)
    pdraw(c, 'Night-before-departure reset', styles['section'], MARGIN_X + 6 * mm, second_y + 37 * mm, CONTENT_W - 12 * mm)
    yy = second_y + 28 * mm
    for item in departure_reset:
        pdraw(c, f'• {item}', styles['body_small'], MARGIN_X + 6 * mm, yy, CONTENT_W - 12 * mm)
        yy -= 7.1 * mm

    links_y = 26 * mm
    round_box(c, MARGIN_X, links_y, CONTENT_W, 28 * mm, fill=WHITE, stroke=BORDER, radius=18)
    pdraw(c, 'Useful official links', styles['section'], MARGIN_X + 6 * mm, links_y + 22 * mm, CONTENT_W - 12 * mm)
    links = official_links[:3]
    button_gap = 4 * mm
    button_w = (CONTENT_W - 12 * mm - 2 * button_gap) / 3
    for i, (title, _desc, _domain, url) in enumerate(links):
        bx = MARGIN_X + 6 * mm + i * (button_w + button_gap)
        draw_text_button(c, bx, links_y + 7 * mm, button_w, 10 * mm, title, url, fill=BLUE, text_color=WHITE, stroke=BLUE)

    draw_footer(c, right_note='Keep the PDF saved locally.')
    c.showPage()


def build_premium_pdf(dest: Path) -> None:
    total_pages = 10
    hero_path = PUBLIC / 'hero.jpg'
    c = canvas.Canvas(str(dest), pagesize=A4)
    c.setTitle('PearlZone Budapest premium itinerary')
    draw_cover(c, hero_path)
    draw_planning_page(c, 2, total_pages)
    for idx, day in enumerate(premium_days, start=3):
        draw_day_page(c, idx, total_pages, day)
    draw_neighborhood_page(c, 8, total_pages)
    draw_baths_page(c, 9, total_pages)
    draw_links_page(c, 10, total_pages)
    c.save()


def build_checklist_pdf(dest: Path) -> None:
    total_pages = 3
    c = canvas.Canvas(str(dest), pagesize=A4)
    c.setTitle('PearlZone Budapest packing checklist')
    checklist_cover(c, 1, total_pages)
    checklist_packing_page(c, 2, total_pages)
    checklist_city_page(c, 3, total_pages)
    c.save()


def render_page(pdf_path: Path, page_number_zero_based: int, out_path: Path, zoom: float = 2.1) -> None:
    doc = fitz.open(pdf_path)
    try:
        page = doc.load_page(page_number_zero_based)
        pix = page.get_pixmap(matrix=fitz.Matrix(zoom, zoom), alpha=False)
        out_path.parent.mkdir(parents=True, exist_ok=True)
        pix.save(out_path)
    finally:
        doc.close()


def render_previews(premium_pdf: Path, checklist_pdf: Path) -> None:
    PREVIEW_PREMIUM.mkdir(parents=True, exist_ok=True)
    PREVIEW_CHECKLIST.mkdir(parents=True, exist_ok=True)
    render_page(premium_pdf, 0, PREVIEW_PREMIUM / 'cover.png')
    render_page(premium_pdf, 2, PREVIEW_PREMIUM / 'day-1.png')
    render_page(premium_pdf, 9, PREVIEW_PREMIUM / 'links.png')
    render_page(checklist_pdf, 0, PREVIEW_CHECKLIST / 'cover.png')
    render_page(checklist_pdf, 1, PREVIEW_CHECKLIST / 'page-2.png')


def main() -> None:
    PRODUCT.mkdir(exist_ok=True)
    DOWNLOADS.mkdir(parents=True, exist_ok=True)
    premium_pdf = PRODUCT / 'budapest-premium-itinerary.pdf'
    checklist_pdf = DOWNLOADS / 'budapest-packing-checklist.pdf'
    build_premium_pdf(premium_pdf)
    build_checklist_pdf(checklist_pdf)
    render_previews(premium_pdf, checklist_pdf)
    print('Generated', premium_pdf)
    print('Generated', checklist_pdf)


if __name__ == '__main__':
    main()
