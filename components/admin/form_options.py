# =====================================================
# FILE: components/admin/form_options.py
# =====================================================

def get_default_brands():

    return [

        "Samsung",
        "Apple",
        "Xiaomi",
        "Realme",
        "OnePlus",
        "Oppo",
        "Vivo",
        "Motorola",
        "Google",
        "Nokia",
        "Infinix",
        "Tecno",
        "iQOO",
        "Poco",
        "Nothing",
        "Asus",
        "Sony",
        "Huawei"
    ]


def get_month_options():

    return [

        "January",
        "February",
        "March",
        "April",
        "May",
        "June",
        "July",
        "August",
        "September",
        "October",
        "November",
        "December"
    ]


def get_year_options():

    return list(
        range(2000, 2031)
    )