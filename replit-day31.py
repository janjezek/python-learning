musicApp = "\033[31m=\033[0m=\033[034m=\033[0m Music app \033[034m=\033[0m=\033[31m=\033[0m"

print(f"{musicApp:^100}")

icons = str("🔥🎵")
artist = "Queen"
song = "Bohemian Rhapsody"

print(f"""
{icons:<8}{song:<40}
{"":<10}{artist:<40}
""")

print(f"""
{"PREV":<50}
{"NEXT":^50}
{"PAUSE":>50}
""")