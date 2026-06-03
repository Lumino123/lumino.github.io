with open('c:/Users/tomas/Downloads/lumowebpage/Lumino.html', 'r', encoding='utf-8') as f:
    html = f.read()

original = html

# ── 1. Add data-i18n attributes to the support-band HTML ─────────────────────

html = html.replace(
    '      <div class="eyebrow">Valsts atbalsts</div>',
    '      <div class="eyebrow" data-i18n="support.eyebrow">Valsts atbalsts</div>'
)
html = html.replace(
    '      <h2>Saņem līdz <span class="serif">15 000 €</span> atbalstu</h2>',
    '      <h2 data-i18n-html="support.h2">Saņem līdz <span class="serif">15 000 €</span> atbalstu</h2>'
)
html = html.replace(
    '      <p class="sub">Latvijas valsts subsidē zaļo enerģiju caur <strong>EKII</strong> programmu. Atbalsts ir pieejams <strong>līdz 2029. gada 31. decembrim</strong> un var segt līdz 70% no iekārtas iegādes cenas. Lumino palīdz sagatavot visu dokumentāciju.</p>',
    '      <p class="sub" data-i18n-html="support.sub">Latvijas valsts subsidē zaļo enerģiju caur <strong>EKII</strong> programmu. Atbalsts ir pieejams <strong>līdz 2029. gada 31. decembrim</strong> un var segt līdz 70% no iekārtas iegādes cenas. Lumino palīdz sagatavot visu dokumentāciju.</p>'
)
# Card 1
html = html.replace(
    '          <div class="sc-label">Saules paneļu un invertora iegādei</div>\n          <div class="sc-max">Līdz 70% no izmaksām</div>',
    '          <div class="sc-label" data-i18n="support.sc1.label">Saules paneļu un invertora iegādei</div>\n          <div class="sc-max" data-i18n="support.sc.pct70">Līdz 70% no izmaksām</div>'
)
# Card 2
html = html.replace(
    '          <div class="sc-label">Gaiss-gaiss un gaiss-ūdens siltumsūknim</div>\n          <div class="sc-max">Jāaizstāj veca kurināmā sistēma</div>',
    '          <div class="sc-label" data-i18n="support.sc2.label">Gaiss-gaiss un gaiss-ūdens siltumsūknim</div>\n          <div class="sc-max" data-i18n="support.sc2.max">Jāaizstāj veca kurināmā sistēma</div>'
)
# Card 3 amount + label + max
html = html.replace(
    '          <div class="sc-amount">līdz <span class="serif">2 500 €</span></div>\n          <div class="sc-label">Elektroenerģijas uzglabāšanas akumulatoram</div>\n          <div class="sc-max">Līdz 70% no izmaksām</div>',
    '          <div class="sc-amount" data-i18n-html="support.sc3.amount">līdz <span class="serif">2 500 €</span></div>\n          <div class="sc-label" data-i18n="support.sc3.label">Elektroenerģijas uzglabāšanas akumulatoram</div>\n          <div class="sc-max" data-i18n="support.sc.pct70">Līdz 70% no izmaksām</div>'
)
# Card 4 amount + label + max
html = html.replace(
    '          <div class="sc-amount">līdz <span class="serif">15 000 €</span></div>\n          <div class="sc-label">Maksimālais atbalsts vienam projektam</div>\n          <div class="sc-max">Kombinējot vairākas iekārtas</div>',
    '          <div class="sc-amount" data-i18n-html="support.sc4.amount">līdz <span class="serif">15 000 €</span></div>\n          <div class="sc-label" data-i18n="support.sc4.label">Maksimālais atbalsts vienam projektam</div>\n          <div class="sc-max" data-i18n="support.sc4.max">Kombinējot vairākas iekārtas</div>'
)
# Note
html = html.replace(
    '        <div>Atbalstu administrē <strong>EKII</strong>. Pieteikšanās notiek elektroniski caur <a href="https://ekii.lv" target="_blank" rel="noopener" style="color:var(--brand);font-weight:600;text-decoration:underline">ekii.lv</a>. Lumino palīdz sagatavot visu dokumentāciju un pieteikumu bez papildu maksas. <a data-go="contact" style="color:var(--brand);font-weight:600;text-decoration:underline">Sazinies ar mums →</a></div>',
    '        <div data-i18n-html="support.note">Atbalstu administrē <strong>EKII</strong>. Pieteikšanās notiek elektroniski caur <a href="https://ekii.lv" target="_blank" rel="noopener" style="color:var(--brand);font-weight:600;text-decoration:underline">ekii.lv</a>. Lumino palīdz sagatavot visu dokumentāciju un pieteikumu bez papildu maksas. <a data-go="contact" style="color:var(--brand);font-weight:600;text-decoration:underline">Sazinies ar mums →</a></div>'
)

# ── 2. Add keys to I18N.lv ────────────────────────────────────────────────────
LV = (
    "'support.eyebrow':'Valsts atbalsts',"
    "'support.h2':'Saņem līdz <span class=\"serif\">15 000 €</span> atbalstu',"
    "'support.sub':'Latvijas valsts subsidē zaļo enerģiju caur <strong>EKII</strong> programmu. Atbalsts ir pieejams <strong>līdz 2029. gada 31. decembrim</strong> un var segt līdz 70% no iekārtas iegādes cenas. Lumino palīdz sagatavot visu dokumentāciju.',"
    "'support.sc1.label':'Saules paneļu un invertora iegādei',"
    "'support.sc.pct70':'Līdz 70% no izmaksām',"
    "'support.sc2.label':'Gaiss-gaiss un gaiss-ūdens siltumsūknim',"
    "'support.sc2.max':'Jāaizstāj veca kurināmā sistēma',"
    "'support.sc3.amount':'līdz <span class=\"serif\">2 500 €</span>',"
    "'support.sc3.label':'Elektroenerģijas uzglabāšanas akumulatoram',"
    "'support.sc4.amount':'līdz <span class=\"serif\">15 000 €</span>',"
    "'support.sc4.label':'Maksimālais atbalsts vienam projektam',"
    "'support.sc4.max':'Kombinējot vairākas iekārtas',"
    "'support.note':'Atbalstu administrē <strong>EKII</strong>. Pieteikšanās notiek elektroniski caur <a href=\"https://ekii.lv\" target=\"_blank\" rel=\"noopener\" style=\"color:var(--brand);font-weight:600;text-decoration:underline\">ekii.lv</a>. Lumino palīdz sagatavot visu dokumentāciju un pieteikumu bez papildu maksas. <a data-go=\"contact\" style=\"color:var(--brand);font-weight:600;text-decoration:underline\">Sazinies ar mums →</a>',"
)
html = html.replace(
    "'common.learn.more':'Uzzināt vairāk →',",
    LV + "\n    'common.learn.more':'Uzzināt vairāk →',"
)

# ── 3. Add keys to I18N.en ────────────────────────────────────────────────────
EN = (
    "'support.eyebrow':'State Support',"
    "'support.h2':'Receive up to <span class=\"serif\">15 000 €</span> in support',"
    "'support.sub':'The Latvian government subsidises green energy through the <strong>EKII</strong> programme. Support is available <strong>until 31 December 2029</strong> and can cover up to 70% of equipment purchase costs. Lumino helps prepare all documentation.',"
    "'support.sc1.label':'For solar panels and inverter',"
    "'support.sc.pct70':'Up to 70% of costs',"
    "'support.sc2.label':'Air-to-air and air-to-water heat pump',"
    "'support.sc2.max':'Old heating system must be replaced',"
    "'support.sc3.amount':'up to <span class=\"serif\">2 500 €</span>',"
    "'support.sc3.label':'For energy storage battery',"
    "'support.sc4.amount':'up to <span class=\"serif\">15 000 €</span>',"
    "'support.sc4.label':'Maximum support per project',"
    "'support.sc4.max':'Combining multiple devices',"
    "'support.note':'Administered by <strong>EKII</strong>. Apply online at <a href=\"https://ekii.lv\" target=\"_blank\" rel=\"noopener\" style=\"color:var(--brand);font-weight:600;text-decoration:underline\">ekii.lv</a>. Lumino helps prepare all documentation and the application at no extra cost. <a data-go=\"contact\" style=\"color:var(--brand);font-weight:600;text-decoration:underline\">Contact us →</a>',"
)
html = html.replace(
    "'common.learn.more':'Learn more →',",
    EN + "\n    'common.learn.more':'Learn more →',"
)

# ── 4. Add keys to I18N.ru ────────────────────────────────────────────────────
RU = (
    "'support.eyebrow':'Господдержка',"
    "'support.h2':'Получите до <span class=\"serif\">15 000 €</span> господдержки',"
    "'support.sub':'Латвийское государство субсидирует зелёную энергию через программу <strong>EKII</strong>. Поддержка доступна <strong>до 31 декабря 2029</strong> года и может покрывать до 70% стоимости оборудования. Lumino помогает подготовить всю документацию.',"
    "'support.sc1.label':'На солнечные панели и инвертор',"
    "'support.sc.pct70':'До 70% от затрат',"
    "'support.sc2.label':'Тепловой насос воздух-воздух и воздух-вода',"
    "'support.sc2.max':'Необходима замена старой системы отопления',"
    "'support.sc3.amount':'до <span class=\"serif\">2 500 €</span>',"
    "'support.sc3.label':'На аккумулятор накопления энергии',"
    "'support.sc4.amount':'до <span class=\"serif\">15 000 €</span>',"
    "'support.sc4.label':'Максимальная поддержка на один проект',"
    "'support.sc4.max':'При сочетании нескольких устройств',"
    "'support.note':'Администрирует <strong>EKII</strong>. Подача заявки — электронно через <a href=\"https://ekii.lv\" target=\"_blank\" rel=\"noopener\" style=\"color:var(--brand);font-weight:600;text-decoration:underline\">ekii.lv</a>. Lumino помогает со всей документацией без доп. платы. <a data-go=\"contact\" style=\"color:var(--brand);font-weight:600;text-decoration:underline\">Свяжитесь с нами →</a>',"
)
html = html.replace(
    "'common.learn.more':'Узнать больше →',",
    RU + "\n    'common.learn.more':'Узнать больше →',"
)

# ── Verify ────────────────────────────────────────────────────────────────────
checks = [
    'data-i18n="support.eyebrow"',
    'data-i18n-html="support.h2"',
    'data-i18n-html="support.sub"',
    'data-i18n="support.sc1.label"',
    'data-i18n="support.sc.pct70"',
    'data-i18n="support.sc2.label"',
    'data-i18n="support.sc2.max"',
    'data-i18n-html="support.sc3.amount"',
    'data-i18n="support.sc3.label"',
    'data-i18n-html="support.sc4.amount"',
    'data-i18n="support.sc4.label"',
    'data-i18n="support.sc4.max"',
    'data-i18n-html="support.note"',
]
for c in checks:
    n = html.count(c)
    print(f'{"OK" if n>0 else "MISSING"} {c} ({n}x)')

with open('c:/Users/tomas/Downloads/lumowebpage/Lumino.html', 'w', encoding='utf-8') as f:
    f.write(html)

print(f'\nDone. {sum(1 for a,b in zip(original,html) if a!=b)} chars changed.')
