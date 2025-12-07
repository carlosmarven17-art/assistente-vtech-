import gradio as gr
import subprocess

def verificar_dispositivo():
    try:
        resultado = subprocess.check_output(["adb", "devices"]).decode()
        if "device" in resultado and "List" not in resultado:
            return "📱 Dispositivo conectado com sucesso!"
        else:
            return "❌ Nenhum dispositivo detectado. Verifique o cabo USB e os drivers."
    except Exception as e:
        return f"Erro: {str(e)}"

def abrir_navegador():
    try:
        subprocess.run(["adb", "shell", "am", "start", "-a", "android.intent.action.VIEW", "-d", "https://www.google.com"])
        return "🌐 Navegador aberto no celular!"
    except Exception as e:
        return f"Erro ao abrir navegador: {str(e)}"

def instalar_apk():
    try:
        subprocess.run(["adb", "install", "frpbypass.apk"])
        return "✅ APK instalado com sucesso!"
    except Exception as e:
        return f"Erro ao instalar APK: {str(e)}"

with gr.Blocks() as assistente:
    gr.Markdown("# 🤖 Assistente Técnica V-Tech")
    gr.Markdown("Automatize tarefas técnicas com um clique!")

    btn1 = gr.Button("🔍 Verificar Dispositivo")
    out1 = gr.Textbox(label="Status")

    btn2 = gr.Button("🌐 Abrir Navegador")
    out2 = gr.Textbox(label="Resultado")

    btn3 = gr.Button("📥 Instalar APK de Bypass")
    out3 = gr.Textbox(label="Resultado")

    btn1.click(verificar_dispositivo, outputs=out1)
    btn2.click(abrir_navegador, outputs=out2)
    btn3.click(instalar_apk, outputs=out3)

assistente.launch()