"""Bilingual case studies and employment history."""

CASES = {
    "golden-cloud": {
        "tags": ("Oracle APEX", "PL/SQL", "Oracle Database", "ORDS", "APEX Office Print"),
        "copy": (
            ("Enterprise project", "Golden Cloud",
             "A bilingual, multi-tenant recruitment SaaS platform covering clients, workers, partner agencies, HR, accounting, and subscriptions.",
             (
                 ("Operational scope", "The platform brought customer records, contracts, worker availability, and recruitment requests into one workflow. Its modules also covered worker rental, service transfers, partner agencies, HR, and accounting."),
                 ("My contribution", "I analyzed requirements with the team, designed the Oracle database schema, and developed the core PL/SQL packages, APEX modules, and reports."),
                 ("Reporting and integration", "I worked on operational reports, document generation with APEX Office Print, and REST APIs with ORDS. The demo shows filtering by country, status, and date."),
             )),
            ("مشروع مؤسسي", "Golden Cloud",
             "منصة SaaS ثنائية اللغة ومتعددة المستأجرين لمكاتب وشركات الاستقدام، تشمل العملاء والعمالة والمكاتب الشريكة والموارد البشرية والحسابات والاشتراكات.",
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


# Public descriptions only; private source repositories are not linked or exported.
_NEW_CASES = {
    "ordermind": {
        "category": "personal",
        "tags": ("Laravel", "PHP", "AI integrations", "JSON Schema", "Evaluation"),
        "flow": (("Order text / image", "Model integration", "Schema + domain validation", "Structured order"), ("نص أو صورة طلب", "تكامل النموذج", "تحقق من المخطط وقواعد المجال", "طلب منظم")),
        "copy": (
            ("Personal project · In development", "OrderMind", "Turning order text and images into structured, validated data with AI model integrations.", (
                ("Idea and ownership", "I conceived and developed OrderMind from scratch as a personal project, using AI-assisted development tools."),
                ("Implementation", "The Laravel/PHP application combines model integrations with schema validation, domain checks, provider routing, retry handling, and cost controls."),
                ("Quality and scope", "An evaluation framework supports extraction-quality assessment. This case study describes development work; no public launch or measured accuracy is claimed."),
            )),
            ("مشروع شخصي · قيد التطوير", "OrderMind", "تحويل نصوص الطلبات وصورها إلى بيانات منظمة قابلة للتحقق باستخدام تكاملات نماذج الذكاء الاصطناعي.", (
                ("الفكرة والملكية", "ابتكرت فكرة OrderMind وطوّرت المشروع من الصفر كمشروع شخصي بمساعدة أدوات الذكاء الاصطناعي."),
                ("التنفيذ", "يجمع تطبيق Laravel وPHP تكاملات النماذج والتحقق من مخطط البيانات وقواعد المجال، مع توجيه المزوّدين وإدارة إعادة المحاولة والتكلفة."),
                ("الجودة ونطاق العرض", "يتضمن المشروع إطارًا لتقييم جودة الاستخراج. تصف هذه الدراسة العمل التطويري، ولا تعلن إطلاقًا عامًا أو أرقام دقة غير مقاسة."),
            )),
        ),
    },
    "z-studio": {
        "category": "personal",
        "tags": ("Python", "FastAPI", "Celery", "Provider adapters", "Background tasks"),
        "flow": (("Content request", "Dependent tasks", "Provider adapters", "Stored outputs + execution status"), ("طلب محتوى", "مهام مترابطة", "موائمات المزوّدين", "مخرجات محفوظة وحالة التنفيذ")),
        "copy": (
            ("Personal project · In development", "Z-STUDIO OS", "A Python backend for coordinating content generation and media processing through provider integrations and background tasks.", (
                ("Idea and ownership", "I conceived and developed Z-STUDIO OS from scratch as a personal project, using AI-assisted development tools."),
                ("Backend engineering", "Python, FastAPI, and Celery support provider adapters, dependency-aware background tasks, execution-state tracking, and output storage."),
                ("Integration scope", "The implementation connects text and media capabilities within traceable workflows. This overview does not claim a public launch or verification of every live provider pipeline."),
            )),
            ("مشروع شخصي · قيد التطوير", "Z-STUDIO OS", "نظام خلفي ببايثون لتنسيق توليد المحتوى ومعالجة الوسائط عبر تكاملات المزوّدين والمهام الخلفية.", (
                ("الفكرة والملكية", "ابتكرت فكرة Z-STUDIO OS وطوّرت المشروع من الصفر كمشروع شخصي بمساعدة أدوات الذكاء الاصطناعي."),
                ("هندسة النظام الخلفي", "يستخدم المشروع Python وFastAPI وCelery لربط موائمات المزوّدين بمهام خلفية مترابطة، مع تتبع حالة التنفيذ وتخزين المخرجات."),
                ("نطاق التكامل", "ينظم قدرات النص والوسائط ضمن مسارات قابلة للتتبع. لا تعني هذه النبذة إطلاقًا عامًا أو التحقق من جميع مسارات المزوّدين الحية."),
            )),
        ),
    },
    "shabic": {
        "category": "enterprise",
        "tags": ("Business applications", "Integrations", "AI-assisted development"),
        "copy": (
            ("Company project", "Shabic", "End-to-end development of a company business application, using AI-assisted development tools.", (
                ("My contribution", "I developed Shabic end to end for a company, using AI-assisted development tools throughout the work."),
                ("Project ownership", "Shabic is company work. This portfolio presents my development role; the source code and company data remain private."),
                ("Engineering approach", "AI-assisted development describes the tools used to build the application. It does not imply that the application itself includes AI features."),
            )),
            ("مشروع شركة", "Shabic", "تطوير تطبيق أعمال لشركة من البداية إلى النهاية بمساعدة أدوات الذكاء الاصطناعي.", (
                ("دوري في المشروع", "تولّيت تطوير Shabic كاملًا لصالح شركة، مستخدمًا أدوات الذكاء الاصطناعي لمساعدتي في أعمال التطوير."),
                ("ملكية المشروع", "Shabic مشروع شركة. يوضح هذا العرض دوري التطويري، مع إبقاء الشيفرة وبيانات الشركة خاصة."),
                ("أسلوب التنفيذ", "المقصود بالتطوير بمساعدة الذكاء الاصطناعي هو الأدوات المستخدمة في البناء؛ ولا يعني ذلك وجود خصائص ذكاء اصطناعي داخل المنتج نفسه."),
            )),
        ),
    },
}
CASES = {"golden-cloud": CASES["golden-cloud"], **_NEW_CASES, **{k: v for k, v in CASES.items() if k != "golden-cloud"}}
