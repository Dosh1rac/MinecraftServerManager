import customtkinter as ctk


class DashboardFrame(ctk.CTkFrame):
    def __init__(self, master, **kwargs):
        super().__init__(master, **kwargs)

        self.configure(fg_color="transparent")

        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)

        self.welcome_label = ctk.CTkLabel(
            self,
            text="Обзор сервера",
            font=ctk.CTkFont(size=24, weight="bold")
        )
        self.welcome_label.grid(
            row=0,
            column=0,
            columnspan=2,
            pady=(20, 20)
        )

        # Карточка статуса
        self.info_card = ctk.CTkFrame(self)
        self.info_card.grid(
            row=1,
            column=0,
            padx=(0, 10),
            pady=10,
            sticky="nsew"
        )

        self.info_card.grid_columnconfigure(0, weight=1)
        self.info_card.grid_columnconfigure(1, weight=1)

        self.status_label = ctk.CTkLabel(
            self.info_card,
            text="Статус сервера:",
            font=ctk.CTkFont(size=16)
        )
        self.status_label.grid(
            row=0,
            column=0,
            padx=20,
            pady=20,
            sticky="w"
        )

        self.status_label_value = ctk.CTkLabel(
            self.info_card,
            text="Online",
            font=ctk.CTkFont(size=16, weight="bold")
        )
        self.status_label_value.grid(
            row=0,
            column=1,
            padx=20,
            pady=20,
            sticky="e"
        )

        # Карточка игроков
        self.players_card = ctk.CTkFrame(self)
        self.players_card.grid(
            row=1,
            column=1,
            padx=(10, 0),
            pady=10,
            sticky="nsew"
        )

        self.players_label = ctk.CTkLabel(
            self.players_card,
            text="Игроки:",
            font=ctk.CTkFont(size=16)
        )
        self.players_label.pack(
            anchor="w",
            padx=20,
            pady=(20, 5)
        )

        self.players_value = ctk.CTkLabel(
            self.players_card,
            text="3 / 20",
            font=ctk.CTkFont(size=20, weight="bold")
        )
        self.players_value.pack(
            anchor="w",
            padx=20,
            pady=(0, 20)
        )