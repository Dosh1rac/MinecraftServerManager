import customtkinter as ctk

from dashboard import DashboardFrame


ctk.set_appearance_mode("System")
ctk.set_default_color_theme("blue")


class App(ctk.CTk):
    def __init__(self):
        super().__init__()

        self.title("Minecraft Manager")
        self.geometry("850x600")

        # Основная сетка
        self.grid_columnconfigure(1, weight=1)
        self.grid_rowconfigure(1, weight=1)

        # Верхняя панель
        self.top_frame = ctk.CTkFrame(
            self,
            height=60,
            corner_radius=0,
            fg_color="transparent"
        )
        self.top_frame.grid(
            row=0,
            column=0,
            columnspan=2,
            sticky="nsew"
        )

        self.title_label = ctk.CTkLabel(
            self.top_frame,
            text="Minecraft Manager",
            font=ctk.CTkFont(size=20, weight="bold")
        )
        self.title_label.pack(
            side="left",
            padx=20,
            pady=10
        )

        # Линия
        self.line = ctk.CTkFrame(
            self,
            height=2,
            corner_radius=0,
            fg_color="gray"
        )
        self.line.grid(
            row=0,
            column=0,
            columnspan=2,
            sticky="s"
        )

        # Sidebar
        self.sidebar_frame = ctk.CTkFrame(
            self,
            width=180,
            corner_radius=0
        )
        self.sidebar_frame.grid(
            row=1,
            column=0,
            sticky="nsew"
        )
        self.sidebar_frame.grid_propagate(False)

        # Кнопки
        self.btn_dashboard = ctk.CTkButton(
            self.sidebar_frame,
            text="Главная",
            command=self.show_dashboard
        )
        self.btn_dashboard.pack(
            padx=20,
            pady=(20, 10),
            fill="x"
        )

        self.btn_players = ctk.CTkButton(
            self.sidebar_frame,
            text="Игроки",
            command=self.show_players
        )
        self.btn_players.pack(
            padx=20,
            pady=10,
            fill="x"
        )

        self.btn_console = ctk.CTkButton(
            self.sidebar_frame,
            text="Консоль",
            command=self.show_console
        )
        self.btn_console.pack(
            padx=20,
            pady=10,
            fill="x"
        )

        self.btn_files = ctk.CTkButton(
            self.sidebar_frame,
            text="Файлы",
            command=self.show_files
        )
        self.btn_files.pack(
            padx=20,
            pady=10,
            fill="x"
        )

        self.btn_bans = ctk.CTkButton(
            self.sidebar_frame,
            text="Баны",
            command=self.show_bans
        )
        self.btn_bans.pack(
            padx=20,
            pady=10,
            fill="x"
        )

        self.btn_logs = ctk.CTkButton(
            self.sidebar_frame,
            text="Логи",
            command=self.show_logs
        )
        self.btn_logs.pack(
            padx=20,
            pady=10,
            fill="x"
        )

        self.btn_backups = ctk.CTkButton(
            self.sidebar_frame,
            text="Бекапы",
            command=self.show_backups
        )
        self.btn_backups.pack(
            padx=20,
            pady=10,
            fill="x"
        )

        self.btn_exit = ctk.CTkButton(
            self.sidebar_frame,
            text="Выход",
            fg_color="transparent",
            border_width=2,
            command=self.quit
        )
        self.btn_exit.pack(
            side="bottom",
            padx=20,
            pady=20,
            fill="x"
        )

        # Основная область
        self.main_frame = ctk.CTkFrame(
            self,
            corner_radius=0,
            fg_color="transparent"
        )
        self.main_frame.grid(
            row=1,
            column=1,
            sticky="nsew",
            padx=20,
            pady=20
        )

        # Страницы
        self.dashboard_screen = DashboardFrame(self.main_frame)

        self.current_screen = None

        self.show_dashboard()

    # -------------------------
    # Переключение страниц
    # -------------------------

    def show_screen(self, screen):
        if self.current_screen is not None:
            self.current_screen.pack_forget()

        screen.pack(
            expand=True,
            fill="both"
        )

        self.current_screen = screen

    def show_dashboard(self):
        self.show_screen(self.dashboard_screen)

    def show_players(self):
        print("Открыта страница Игроки")

    def show_console(self):
        print("Открыта страница Консоль")

    def show_files(self):
        print("Открыта страница Файлы")

    def show_bans(self):
        print("Открыта страница Баны")

    def show_logs(self):
        print("Открыта страница Логи")

    def show_backups(self):
        print("Открыта страница Бекапы")


if __name__ == "__main__":
    app = App()
    app.mainloop()