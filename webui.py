from dotenv import load_dotenv
load_dotenv()
import argparse
from src.webui.interface import theme_map, create_ui


def main():
    parser = argparse.ArgumentParser(description="Gradio WebUI for Browser Agent")
    parser.add_argument("--ip", type=str, default="127.0.0.1", help="IP address to bind to")
    parser.add_argument("--port", type=int, default=7788, help="Port to listen on")
    parser.add_argument("--theme", type=str, default="Ocean", choices=theme_map.keys(), help="Theme to use for the UI")
    parser.add_argument("--username", type=str, default="admin", help="Username for authentication")
    parser.add_argument("--password", type=str, default="admin", help="Password for authentication")
    args = parser.parse_args()

    demo = create_ui(theme_name=args.theme)

    # Add authentication
    auth = (args.username, args.password)

    demo.queue().launch(
        server_name=args.ip,
        server_port=args.port,
        auth=auth  # Enforce authentication
    )


if __name__ == '__main__':
    main()
