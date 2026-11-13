"""Bilingual case studies and employment history."""

CASES = {
    "golden-cloud": {
        "tags": ("Oracle APEX", "PL/SQL", "Oracle Database", "ORDS", "APEX Office Print"),
        "copy": (
            ("Enterprise project", "Golden Cloud",
             "A bilingual platform for recruitment agencies covering clients, workers, partner agencies, HR, and accounting.",
             (
                 ("Operational scope", "The platform brought customer records, contracts, worker availability, and recruitment requests into one workflow. Its modules also covered worker rental, service transfers, partner agencies, HR, and accounting."),
                 ("My contribution", "I analyzed requirements with the team, designed the Oracle database schema, and developed the core PL/SQL packages, APEX modules, and reports."),
                 ("Reporting and integration", "I worked on operational reports, document generation with APEX Office Print, and REST APIs with ORDS. The demo shows filtering by country, status, and date."),
             )),
            ("مشروع مؤسسي", "Golden Cloud",
             "منصة ثنائية اللغة لمكاتب وشركات الاستقدام تشمل العملاء والعمالة والمكاتب الشريكة والموارد البشرية والحسابات.",
             (
                 ("نطاق المنصة", "جمعت المنصة سجلات العملاء والعقود وتوفّر العمالة وطلبات الاستقدام في مسار عمل واحد. وشملت وحداتها تأجير العمالة ونقل الخدمات والمكاتب الشريكة والموارد البشرية والحسابات."),
                 ("دوري في المشروع", "حلّلت المتطلبات مع الفريق، وصمّمت قاعدة بيانات Oracle، وطوّرت حزم PL/SQL الأساسية ووحدات Oracle APEX والتقارير."),
                 ("التقارير والتكامل", "عملت على تقارير التشغيل وتوليد المستندات باستخدام APEX Office Print وواجهات REST باستخدام ORDS. يوضّح الفيديو فلترة التقارير حسب الدولة والحالة والتاريخ."),
             )),
        ),
    },
    "financial-ledger": {
        "repo": "financial-ledger-api",
        "tags": ("Python", "FastAPI", "REST", "Double-entry accounting"),
        "copy": (
            ("Public demo", "Financial Ledger API",
             "A double-entry accounting demo with vouchers, a chart of accounts, and trial balance reporting.",
             (
                 ("Accounting workflow", "The API models a chart of accounts, voucher workflows, and double-entry journals. The trial balance illustrates how debit and credit entries feed reporting."),
                 ("Oracle experience", "The accompanying case study describes the Oracle experience behind the demo and provides context for the public implementation."),
             )),
            ("نموذج برمجي عام", "Financial Ledger API",
             "نموذج محاسبة بالقيد المزدوج يضم السندات ودليل الحسابات وميزان المراجعة.",
             (
                 ("سير العمل المحاسبي", "تمثّل الواجهة البرمجية دليل الحسابات ومسار السندات والقيود المحاسبية المزدوجة. ويبيّن ميزان المراجعة كيف تنتقل القيود المدينة والدائنة إلى التقارير."),
                 ("الخبرة على Oracle", "تشرح دراسة الحالة المرفقة الخبرة على Oracle التي استند إليها النموذج المنشور."),
             )),
        ),
    },
    "loan-management": {
        "repo": "loan-management-system",
        "tags": ("Python", "FastAPI", "REST", "Microfinance"),
        "copy": (
            ("Public demo", "Loan Management System",
             "A microfinance demo for loan amortization, repayment schedules, and credit workflows.",
             (
                 ("Loan workflow", "The demo illustrates credit workflows and how loan terms drive amortization and repayment schedules."),
                 ("Oracle experience", "The accompanying case study describes the Oracle microfinance experience that informed the public implementation."),
             )),
            ("نموذج برمجي عام", "Loan Management System",
             "نموذج للتمويل الأصغر يغطّي احتساب أقساط القروض وجداول السداد وسير العمل الائتماني.",
             (
                 ("سير عمل القروض", "يوضّح النموذج مسار العمل الائتماني وكيف تُستخدم شروط القرض في احتساب الأقساط وإعداد جداول السداد."),
                 ("الخبرة على Oracle", "تشرح دراسة الحالة المرفقة خبرة تطوير أنظمة التمويل الأصغر على Oracle التي استند إليها النموذج المنشور."),
             )),
        ),
    },
}

ROLES = (
    (
        ("Golden Network for Information Systems Technology · Jeddah",
         "Software Engineer (Oracle APEX &amp; PL/SQL)", "Aug 2022 – Aug 2026",
         "Analyzed requirements, designed Oracle database schemas, and built PL/SQL packages, Oracle APEX modules, reports, and REST integrations for the Golden Cloud recruitment platform."),
        ("National Microfinance Foundation · Sanaa",
         "Senior Oracle APEX &amp; PL/SQL Developer", "Apr 2020 – Aug 2022",
         "Developed applications for loans, accounting, and fund transfers, and built ORDS APIs for mobile integration."),
        ("Abu Nabil Alqaramani for Trading &amp; Investment Co. · Sanaa",
         "Oracle APEX &amp; PL/SQL Developer", "Jan 2018 – Mar 2020",
         "Built Oracle APEX applications, PL/SQL business logic, and operational reports."),
        ("ADWAR Youth Development", "Database Management Assistant", "Jan 2017 – Dec 2017",
         "Supported database management and reporting."),
        ("ADWAR Youth Development", "Data Entry Officer", "Jan 2016 – Dec 2016",
         "Maintained program records and supported data quality."),
    ),
    (
        ("الشبكة الذهبية لتقنية نظم المعلومات · جدة",
         "مهندس برمجيات Oracle APEX وPL/SQL", "أغسطس 2022 – أغسطس 2026",
         "حلّلت المتطلبات وصمّمت قاعدة بيانات Oracle وطوّرت حزم PL/SQL ووحدات Oracle APEX والتقارير وتكاملات REST لمنصة Golden Cloud للاستقدام."),
        ("المؤسسة الوطنية للتمويل الأصغر · صنعاء",
         "مطوّر أول Oracle APEX وPL/SQL", "أبريل 2020 – أغسطس 2022",
         "طوّرت تطبيقات القروض والمحاسبة والتحويلات المالية، وواجهات ORDS للتكامل مع تطبيقات الهاتف."),
        ("شركة أبو نبيل القرماني للتجارة والاستثمار · صنعاء",
         "مطوّر Oracle APEX وPL/SQL", "يناير 2018 – مارس 2020",
         "طوّرت تطبيقات Oracle APEX وقواعد العمل في PL/SQL والتقارير التشغيلية."),
        ("أدوار لتنمية الشباب", "مساعد إدارة قواعد البيانات", "يناير 2017 – ديسمبر 2017",
         "ساندت إدارة قواعد البيانات وإعداد التقارير."),
        ("أدوار لتنمية الشباب", "مسؤول إدخال البيانات", "يناير 2016 – ديسمبر 2016",
         "حدّثت سجلات البرامج وساعدت في ضبط جودة البيانات."),
    ),
)
