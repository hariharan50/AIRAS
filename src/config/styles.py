CUSTOM_CSS = """
<style>
    :root {
        --primary-color: #4CAF50;
        --secondary-color: #2196F3;
        --dark-bg: #1a1a1a;
        --light-bg: #f5f5f5;
    }

    [data-testid="stSidebar"] {
        background: linear-gradient(180deg, var(--primary-color), var(--secondary-color)) !important;
        color: white !important;
    }

    .sidebar-title {
        font-size: 24px !important;
        font-weight: bold !important;
        margin-bottom: 20px !important;
        color: white !important;
    }

    .menu-item {
        padding: 10px 15px !important;
        border-radius: 5px !important;
        margin: 5px 0 !important;
        transition: all 0.3s !important;
    }

    .menu-item:hover {
        background: rgba(255,255,255,0.1) !important;
    }

    .detail-box {
        border: 1px solid #e0e0e0;
        border-radius: 10px;
        padding: 20px;
        margin: 15px 0;
        background: #ffffff;
    }

    .summary-box {
        background: #f8f9fa;
        border-left: 4px solid var(--primary-color);
        padding: 15px;
        margin: 10px 0;
    }
</style>
"""