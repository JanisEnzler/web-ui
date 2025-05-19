import gradio as gr

from src.webui.webui_manager import WebuiManager
from src.webui.components.agent_settings_tab import create_agent_settings_tab
from src.webui.components.browser_settings_tab import create_browser_settings_tab
from src.webui.components.browser_use_agent_tab import create_browser_use_agent_tab
from src.webui.components.deep_research_agent_tab import create_deep_research_agent_tab
from src.webui.components.load_save_config_tab import create_load_save_config_tab

# Create a custom theme with system fonts instead of Google Fonts
custom_theme = gr.themes.Base(
    primary_hue="green",
    secondary_hue="gray",
    neutral_hue="gray",
).set(
    background_fill_primary="#000000",
    body_text_color="#30363d",
    block_background_fill="#0D1117",
    button_primary_background_fill="#2EA043",
    button_primary_text_color="#FFFFFF",
    border_color_primary="#30363d",
    block_border_width="1px",
)

# Only keep your custom theme
theme_map = {
    "Custom": custom_theme
}


def create_ui(theme_name="Custom"):
    css = """
    .gradio-container {
        width: 70vw !important; 
        max-width: 70% !important; 
        margin-left: auto !important;
        margin-right: auto !important;
        padding-top: 10px !important;
    }
    .header-text {
        text-align: center;
        margin-bottom: 20px;
        color: #FFFFFF !important;
    }
    .header-text h1, 
    .header-text h2, 
    .header-text h3, 
    .header-text h4, 
    .header-text h5, 
    .header-text h6,
    .header-text p {
        color: #FFFFFF !important;
    }
    .bug-icon {
        display: inline-block;
        vertical-align: middle;
        margin-right: 10px;
        margin-top: 16px;
    }
    
    
    .title-with-icon {
        display: flex;
        align-items: center;
        justify-content: center;
    }
    
    .title-with-icon h1 {
        display: inline-block;
        margin-left: 10px;
    }
    .tab-header-text {
        text-align: center;
    }
    .theme-section {
        margin-bottom: 10px;
        padding: 15px;
        border-radius: 10px;
    }
    /* Apply system font to all elements */
    * {
        font-family: -apple-system, BlinkMacSystemFont, Segoe UI, Helvetica, Arial, sans-serif !important;
    }
    /* Code elements should use monospace */
    code, pre {
        font-family: SFMono-Regular, Consolas, Liberation Mono, Menlo, monospace !important;
    }
    """

    ui_manager = WebuiManager()

    with gr.Blocks(
            title="Bugtracker AI", theme=custom_theme, css=css,
    ) as demo:
        with gr.Row():
            gr.HTML(
                """
                <div class="header-text">
                    <div class="title-with-icon">
                        <svg xmlns="http://www.w3.org/2000/svg" width="32" height="32" viewBox="0 0 24 24" fill="none" 
                            stroke="#2EA043" stroke-width="2" stroke-linecap="round" stroke-linejoin="round" 
                            class="bug-icon">
                            <path d="m8 2 1.88 1.88"></path>
                            <path d="M14.12 3.88 16 2"></path>
                            <path d="M9 7.13v-1a3.003 3.003 0 1 1 6 0v1"></path>
                            <path d="M12 20c-3.3 0-6-2.7-6-6v-3a4 4 0 0 1 4-4h4a4 4 0 0 1 4 4v3c0 3.3-2.7 6-6 6"></path>
                            <path d="M12 20v-9"></path>
                            <path d="M6.53 9C4.6 8.8 3 7.1 3 5"></path>
                            <path d="M6 13H2"></path>
                            <path d="M3 21c0-2.1 1.7-3.9 3.8-4"></path>
                            <path d="M20.97 5c0 2.1-1.6 3.8-3.5 4"></path>
                            <path d="M22 13h-4"></path>
                            <path d="M17.2 17c2.1.1 3.8 1.9 3.8 4"></path>
                        </svg>
                        <h1>Bugtracker AI</h1>
                    </div>
                    <h3>Test your website with AI agents</h3>
                </div>
                """
            )

        with gr.Tabs() as tabs:
            with gr.TabItem("Agent Settings"):
                create_agent_settings_tab(ui_manager)

            with gr.TabItem("Browser Settings"):
                create_browser_settings_tab(ui_manager)

            with gr.TabItem("Run Agent"):
                create_browser_use_agent_tab(ui_manager)


    return demo
