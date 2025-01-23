from dataclasses import dataclass, field

from nicegui import ui


@dataclass
class Batter:
    name: str = ""
    balls: int = 0
    score: int = 0

    def ball(self, runs: int):
        self.balls += 1
        self.score += runs

    def markdown(self) -> str:
        return f"{self.name} .... {self.score} ({self.balls})"

    def html(self) -> str:
        return f"<div style='display: flex; justify-content: space-between; width: 180px;'><div><b>{self.name}</b></div><div>{self.score} ({self.balls})</div>"

    def __str__(self) -> str:
        return self.html()


@dataclass
class ScoreCard:
    batters: list[Batter] = field(default_factory=list)
    striker: int = 0
    non_striker: int = 1

    def add_ball(self, runs: int):
        self.batters[self.striker].ball(runs)
        if runs % 2:
            self.striker, self.non_striker = self.non_striker, self.striker


scorecard = ScoreCard(
    batters=[
        Batter(name="Alice"),
        Batter(name="Bob"),
        Batter(name="Charlie"),
        Batter(name="Derek"),
        Batter(name="Ernie"),
        Batter(name="Frank"),
        Batter(name="George"),
        Batter(name="Harry"),
        Batter(name="Ivan"),
        Batter(name="Jim"),
        Batter(name="Ken"),
    ]
)

BALLS = [0, 1, 2, 3, 4, 6]

with ui.row():
    with ui.column():
        with ui.card():
            with ui.grid(columns=6):
                for i in BALLS:
                    ui.button(text=str(i), on_click=lambda i=i: scorecard.add_ball(i)).style("height: 70px;").props(
                        "color=black"
                    )

                for i in BALLS:
                    ui.button(text=f"w+{i}", on_click=lambda: scorecard.add_ball(i))

                for i in BALLS:
                    ui.button(text=f"nb+{i}", on_click=lambda: scorecard.add_ball(i))

                for i in BALLS:
                    ui.button(text=f"b+{i}", on_click=lambda: scorecard.add_ball(i))

    with ui.column():
        with ui.card().style("width: 200px;"):
            ui.html("").bind_content_from(scorecard, "batters", backward=lambda x: str(x[0]))
            ui.html("").bind_content_from(scorecard, "batters", backward=lambda x: str(x[1]))
            ui.html("").bind_content_from(scorecard, "batters", backward=lambda x: str(x[2]))
            ui.html("").bind_content_from(scorecard, "batters", backward=lambda x: str(x[3]))
            ui.html("").bind_content_from(scorecard, "batters", backward=lambda x: str(x[4]))
            ui.html("").bind_content_from(scorecard, "batters", backward=lambda x: str(x[5]))
            ui.html("").bind_content_from(scorecard, "batters", backward=lambda x: str(x[6]))
            ui.html("").bind_content_from(scorecard, "batters", backward=lambda x: str(x[7]))
            ui.html("").bind_content_from(scorecard, "batters", backward=lambda x: str(x[8]))
            ui.html("").bind_content_from(scorecard, "batters", backward=lambda x: str(x[9]))
            ui.html("").bind_content_from(scorecard, "batters", backward=lambda x: str(x[10]))

ui.run()
