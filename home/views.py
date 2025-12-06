# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""

from django.shortcuts import render


def index(request):
    qr_stands = [
        {"address": "Ленина 1", "leads": 1, "orders": 0},
        {"address": "Ленина 2", "leads": 2, "orders": 1},
    ]

    targeting_channels = [
        {
            "name": "Лиды по таргету",
            "leads": 5,
            "conversion": 0,
            "spent": 100,
            "projected_spend": 120,
            "forecast_orders": 1,
        },
        {
            "name": "Яндекс директ",
            "leads": 1,
            "conversion": 1,
            "spent": 300,
            "projected_spend": 360,
            "forecast_orders": 2,
        },
        {
            "name": "Авито",
            "leads": 7,
            "conversion": 5,
            "spent": 500,
            "projected_spend": 600,
            "forecast_orders": 6,
        },
        {
            "name": "VK",
            "leads": 3,
            "conversion": 4,
            "spent": 800,
            "projected_spend": 960,
            "forecast_orders": 5,
        },
        {
            "name": "Еще что-либо",
            "leads": 8,
            "conversion": 3,
            "spent": 900,
            "projected_spend": 1080,
            "forecast_orders": 4,
        },
        {
            "name": "Еще что-либо",
            "leads": 6,
            "conversion": 1,
            "spent": 1000,
            "projected_spend": 1200,
            "forecast_orders": 1,
        },
    ]

    product_analytics = {
        "Тольятти": [
            {
                "model": "L1",
                "colors": [
                    {"color": "белый", "share_sales": 20, "share_colors": 20, "share_models": 20, "rub": 0, "qty": 0},
                    {"color": "серый", "share_sales": 30, "share_colors": 30, "share_models": 30, "rub": 0, "qty": 0},
                    {"color": "зеленый", "share_sales": 50, "share_colors": 50, "share_models": 50, "rub": 0, "qty": 0},
                    {"color": "красный", "share_sales": 0, "share_colors": 0, "share_models": 0, "rub": 0, "qty": 0},
                ],
            },
            {"model": "L2", "colors": []},
            {"model": "L3", "colors": []},
            {"model": "L4", "colors": []},
        ],
        "Сызрань": [],
        "Ульяновск": [],
        "Пермь": [],
    }

    expense_lines = [
        {"name": "Основные статьи", "amount": 100},
        {"name": "Закупка", "amount": None},
        {"name": "Логистика", "amount": None},
        {"name": "Эквайринг", "amount": None},
        {"name": "Обслуживане счета", "amount": None},
        {"name": "Комиссии партнерам", "amount": 500},
        {"name": "Брак", "amount": None},
        {"name": "Таргетинг", "amount": None},
        {"name": "Зарплата", "amount": None},
        {"name": "Связь", "amount": 300},
        {"name": "Канцелярия", "amount": None},
    ]

    total_expenses = sum([item["amount"] for item in expense_lines if item["amount"]])
    sales_total = 21500
    taxes = 2300

    context = {
        "qr_stands": qr_stands,
        "targeting_channels": targeting_channels,
        "product_analytics": product_analytics,
        "expense_lines": expense_lines,
        "totals": {
            "expenses": total_expenses,
            "sales": sales_total,
            "operating_profit": sales_total - total_expenses,
            "cash_balance": sales_total - total_expenses,
            "net_profit": sales_total - total_expenses - taxes,
            "taxes": taxes,
        },
        "manager_responsiveness": {
            "first_reply": "6 минут",
            "avg_reply": "11 минут",
            "lost_leads": 2,
            "callback_stats": "дозвон 78% / недозвон 22%",
            "quality_score": "AI: 8.5/10",
        },
        "crm_compliance": {
            "tasks_completed": 86,
            "tasks_overdue": 9,
            "stuck_leads": 3,
            "heavy_users": ["Менеджер А", "Менеджер D"],
        },
        "manager_effectiveness": [
            {
                "name": "Менеджер А",
                "picked": 24,
                "processed": 21,
                "measure_conversion": 62,
                "order_conversion": 28,
                "avg_check": 54000,
                "avg_margin": 0.31,
                "rating": 8.7,
            },
            {
                "name": "Менеджер B",
                "picked": 19,
                "processed": 17,
                "measure_conversion": 55,
                "order_conversion": 24,
                "avg_check": 49800,
                "avg_margin": 0.27,
                "rating": 8.2,
            },
        ],
        "site_funnel": {
            "by_model": [
                {"model": "L1", "color": "белый", "region": "Тольятти", "depth": 3, "clicks": 110},
                {"model": "L1", "color": "серый", "region": "Пермь", "depth": 2, "clicks": 75},
            ],
            "by_device": [
                {"device": "Desktop", "sessions": 240, "orders": 12},
                {"device": "Mobile", "sessions": 410, "orders": 9},
            ],
            "by_age": [
                {"age": "25-34", "sessions": 180, "orders": 7},
                {"age": "35-44", "sessions": 260, "orders": 9},
            ],
            "utm": [
                {"source": "yandex", "sessions": 220, "orders": 8},
                {"source": "vk", "sessions": 190, "orders": 6},
            ],
        },
        "builder_report": {
            "visualization": 72,
            "color_changed": 54,
            "model_changed": 41,
            "options_added": 33,
            "multi_variations": 16,
            "top_built": ["L1 белый стекло", "L2 серый без стекла"],
            "abandoned": ["L3 зеленый стекло", "L1 красный панель"],
        },
        "site_health": {
            "load_speed": "1.9s среднее",
            "console_errors": 0,
            "not_found": 2,
            "bounce_points": ["карточка L3", "конфигуратор шаг 3"],
            "ux_notes": "люди уходят при выборе стекла",
        },
        "inventory_checks": [
            {"title": "Есть в CRM, нет в 1С", "count": 4},
            {"title": "Есть в 1С, нет в CRM", "count": 3},
            {"title": "Нет цены поставщика", "count": 2},
            {"title": "Нет размера/характеристики", "count": 5},
        ],
        "production_control": [
            {"title": "Заказы >5 дней без статуса", "count": 2},
            {"title": "В производстве > норматива", "count": 1},
            {"title": "Готовы, не отгружены >3 дней", "count": 1},
            {"title": "Отгружено с просрочкой", "count": 3},
            {"title": "Отмены ЛИСТ", "count": 0},
        ],
        "claims": {
            "types": [
                {"type": "Фабрика", "reason": "царапины", "loss": 12000, "close_time": "3 дня"},
                {"type": "Доставка", "reason": "вмятина", "loss": 8000, "close_time": "2 дня"},
            ],
            "defect_share": [
                {"model": "L1", "rate": 1.2},
                {"model": "L2", "rate": 0.6},
            ],
        },
        "sales_funnel": [
            {"stage": "Лид", "units": 32, "value": 0},
            {"stage": "Замер", "units": 18, "value": 0},
            {"stage": "Заказ", "units": 12, "value": 640000},
            {"stage": "Оплата", "units": 10, "value": 520000},
            {"stage": "Производство", "units": 8, "value": 430000},
            {"stage": "Отгрузка", "units": 7, "value": 380000},
        ],
        "abc_xyz": [
            {"group": "A", "share": 80, "stability": "X"},
            {"group": "B", "share": 15, "stability": "Y"},
            {"group": "C", "share": 5, "stability": "Z"},
        ],
        "average_ticket": [
            {"dimension": "Город", "items": [{"label": "Тольятти", "value": 54000}, {"label": "Пермь", "value": 51000}]},
            {"dimension": "Стенд", "items": [{"label": "Ленина 1", "value": 52000}, {"label": "Ленина 2", "value": 49500}]},
            {"dimension": "Модель", "items": [{"label": "L1", "value": 50500}, {"label": "L2", "value": 56000}]},
        ],
        "ltv": [
            {"label": "Средний LTV по региону", "value": 82000},
            {"label": "LTV по таргетированным каналам", "value": 76000},
        ],
        "forecast": [
            {"period": "7 дней", "projection": 18},
            {"period": "30 дней", "projection": 74},
            {"period": "3 месяца", "projection": 210},
        ],
        "lead_quality": [
            {"label": "Горячие", "criteria": "намерение купить <7 дней", "share": 32},
            {"label": "Теплые", "criteria": "изменили модель/цвет", "share": 44},
            {"label": "Холодные", "criteria": "1 визит, без конструктора", "share": 24},
        ],
        "traffic_quality": [
            {"metric": "Боты/накрутка", "value": "1.8%"},
            {"metric": "Стоимость уникального клиента", "value": "650 ₽"},
            {"metric": "Стоимость клиента дошедшего до конструктора", "value": "1200 ₽"},
        ],
        "target_math": [
            {"metric": "ROI", "value": "162%"},
            {"metric": "ROMI", "value": "138%"},
            {"metric": "CPL", "value": "850 ₽"},
            {"metric": "CPO", "value": "5300 ₽"},
            {"metric": "CAC", "value": "7800 ₽"},
        ],
        "payment_calendar": [
            {"title": "Поставщики", "amount": 240000, "date": "в течение недели"},
            {"title": "Поступления от клиентов", "amount": 180000, "date": "в течение недели"},
            {"title": "Предстоящие расходы", "amount": 95000, "date": "в течение недели"},
        ],
        "cash_flow": [
            {"period": "Неделя", "inflow": 320000, "outflow": 215000},
            {"period": "Месяц", "inflow": 1240000, "outflow": 980000},
        ],
        "profit_loss": {
            "gross": sales_total - 7200,
            "operating": sales_total - total_expenses,
            "ebitda": sales_total - total_expenses,
            "net": sales_total - total_expenses - taxes,
        },
        "margin_breakdown": [
            {"dimension": "Модель", "items": [{"label": "L1", "margin": "32%"}, {"label": "L2", "margin": "28%"}]},
            {"dimension": "Город", "items": [{"label": "Тольятти", "margin": "30%"}, {"label": "Пермь", "margin": "26%"}]},
            {"dimension": "Канал", "items": [{"label": "QR стенды", "margin": "24%"}, {"label": "Таргет", "margin": "29%"}]},
        ],
    }

    return render(request, "pages/index.html", context)
