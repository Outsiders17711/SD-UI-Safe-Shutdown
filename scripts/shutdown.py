from modules import shared, script_callbacks
from modules import script_callbacks
import gradio as gr
import os


js = """
function close_window() {
    if (confirm("Close the application?")) {
        document.body.innerHTML = '';
        document.body.style.height = '95%';
        document.body.style.display = 'flex';
        document.body.style.justifyContent = 'center';
        document.body.style.alignItems = 'center';

        const darkModeMediaQuery = window.matchMedia('(prefers-color-scheme: dark)');
        if (darkModeMediaQuery.matches) {
            document.body.style.backgroundColor = 'black';  // Dark Mode
        } else {
            document.body.style.backgroundColor = 'white';  // Light Mode
        }

        var buttonContainer = document.createElement('div');
        buttonContainer.style.display = 'flex';
        buttonContainer.style.justifyContent = 'center';
        buttonContainer.style.gap = '1em';
        document.body.appendChild(buttonContainer);

        function applyButtonStyles(button) {
            button.style.padding = '15px 30px';
            button.style.backgroundColor = '#d49013';
            button.style.color = 'white';
            button.style.border = 'none';
            button.style.cursor = 'pointer';
            button.style.borderRadius = '10px';
            button.style.marginRight = '10px';
            button.style.fontSize = '18px';
            button.style.fontWeight = 'bold';
            button.style.textTransform = 'uppercase';
            button.style.boxShadow = '0 2px 6px rgba(0, 0, 0, 0.3)';
            button.style.transition = 'transform 0.2s';
        }

        function applyButtonHoverStyles(button) {
            button.addEventListener('mouseover', function() {
                button.style.transform = 'scale(1.1)';
            });

            button.addEventListener('mouseout', function() {
                button.style.transform = 'scale(1)';
            });
        }

        var reloadButton = document.createElement('button');
        reloadButton.textContent = 'Reload';
        reloadButton.classList.add('button');
        reloadButton.addEventListener('click', function() {
            location.reload();
        });
        applyButtonStyles(reloadButton);
        applyButtonHoverStyles(reloadButton);
        buttonContainer.appendChild(reloadButton);

        var closeButton = document.createElement('button');
        closeButton.textContent = 'Close';
        closeButton.classList.add('button');
        closeButton.addEventListener('click', function() {
            window.close();
        });
        applyButtonStyles(closeButton);
        applyButtonHoverStyles(closeButton);
        buttonContainer.appendChild(closeButton);

        return true;
    } else {
        return false;
    }
}
"""


def stop_button(component, **kwargs):
    after_this_compo = "setting_{}".format(shared.opts.data["quicksettings_list"][-1])

    if kwargs.get("elem_id") == after_this_compo:
        with gr.Row(elem_id="quicksettings", variant="compact"):
            btn = gr.Button("Exit ⭕", elem_id="stop_button", size="sm", variant="stop")
            hidden_checkbox = gr.Checkbox(visible=False)

            def when(hidden_state):
                if hidden_state:
                    os._exit(0)
                return False

            btn.click(when, hidden_checkbox, hidden_checkbox, _js=js)


script_callbacks.on_after_component(stop_button)
