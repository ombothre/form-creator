import random
from cluster import CLUSTERS  # Ensure this module exists and is accessible

def generate_form():
    n = random.randint(1, 7)
    random.seed(n)
    optional_keys = list(CLUSTERS.keys())
    optional_keys.remove("bio_data")  # bio_data always included
    selected = random.sample(optional_keys, k=n)
    html_form = CLUSTERS["bio_data"] + "\n\n" + "\n\n".join(CLUSTERS[k] for k in selected)
    return html_form

def wrap_with_html(form_body):
    return f"""
    <html>
    <head>
    <style>
        body {{
            font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
            background-color: #ffffff;
            color: #2c3e50;
            padding: 40px;
            font-size: 13pt;
            line-height: 1.6;
        }}

        h3 {{
            font-size: 18pt;
            text-align: center;
            background-color: #f4f6f8;
            border-bottom: 2px solid #2c3e50;
            padding: 10px 0;
            margin-top: 40px;
        }}

        form {{
            max-width: 900px;
            margin: auto;
            padding: 30px;
            background: #fff;
            border: 1px solid #ccc;
            border-radius: 6px;
        }}

        .form-row {{
            display: flex;
            flex-wrap: wrap;
            gap: 20px;
            margin-bottom: 20px;
        }}

        .form-group {{
            flex: 1;
            min-width: 200px;
        }}

        label {{
            font-weight: bold;
            display: block;
            margin-bottom: 5px;
        }}

        input[type="text"], input[type="date"], input[type="number"], input[type="email"], select {{
            width: 100%;
            padding: 10px;
            border: 1px solid #ccc;
            border-radius: 4px;
            font-size: 12pt;
            background-color: #fafafa;
        }}

        input[type="checkbox"] {{
            transform: scale(1.2);
            margin-right: 8px;
        }}

        .checkbox-group {{
            display: flex;
            align-items: center;
            margin-bottom: 10px;
        }}

        @media print {{
            body {{
                padding: 0;
                font-size: 12pt;
            }}
            form {{
                border: none;
                padding: 0;
                box-shadow: none;
            }}
            input[type="text"] {{
                border: 1px solid #000;
                background: transparent;
            }}
        }}
    </style>
    </head>
    <body>
    <form>
    {form_body}
    </form>
    </body>
    </html>
    """