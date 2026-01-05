import numpy as np
from manim import *


class EconomicGrowth(Scene):
    def construct(self):
        # Title
        title = Text("The Elegant Theory of Economic Growth", font_size=48)
        self.play(Write(title))
        self.wait(2)
        self.play(FadeOut(title))

        # Introduction section
        self.introduction()
        self.wait(1)

        # Solow model
        self.solow_production_function()
        self.wait(1)

        self.assumptions()
        self.wait(1)

        self.cobb_douglas()
        self.wait(1)

        self.capital_accumulation()

    def introduction(self):
        """Introduction with GDP growth plot"""
        # Create axes for GDP growth
        axes = Axes(
            x_range=[1900, 2020, 20],
            y_range=[0, 60000, 10000],
            x_length=10,
            y_length=6,
            axis_config={"include_numbers": True},
            tips=False,
        )

        # Labels
        x_label = axes.get_x_axis_label("Year", edge=DOWN, direction=DOWN)
        y_label = axes.get_y_axis_label("GDP per capita", edge=LEFT, direction=LEFT)

        # Exponential growth curve
        growth_curve = axes.plot(
            lambda x: 1000 * np.exp(0.02 * (x - 1900)), color=BLUE, x_range=[1900, 2020]
        )

        # Add some year markers
        years = [1920, 1950, 1980, 2010]
        dots = VGroup(
            *[
                Dot(axes.c2p(year, 1000 * np.exp(0.02 * (year - 1900))), color=RED)
                for year in years
            ]
        )
        year_labels = VGroup(
            *[
                Text(str(year), font_size=20).next_to(
                    axes.c2p(year, 1000 * np.exp(0.02 * (year - 1900))), UP
                )
                for year in years
            ]
        )

        self.play(Create(axes), Write(x_label), Write(y_label))
        self.play(Create(growth_curve), run_time=3)
        self.play(FadeIn(dots), Write(year_labels))
        self.wait(2)
        self.play(FadeOut(axes, x_label, y_label, growth_curve, dots, year_labels))

    def solow_production_function(self):
        """Production function introduction"""
        # Show Y_t then Y
        y_t = MathTex("Y_t", font_size=96)
        self.play(Write(y_t))
        self.wait(1)

        y = MathTex("Y", font_size=96)
        self.play(Transform(y_t, y))
        self.wait(1)
        self.play(y_t.animate.scale(0.5).to_edge(UP))

        # Production function
        prod_func = MathTex("Y = F(L, K)", font_size=60)
        self.play(Write(prod_func))
        self.wait(2)
        self.play(FadeOut(y_t, prod_func))

    def assumptions(self):
        """Show the assumptions about the production function"""
        # Container for assumptions on the left
        assumptions_list = VGroup().to_edge(LEFT).shift(UP * 2)

        # Assumption 1: Continuity
        assumption1_title = Text("Assumption 1: Continuity", font_size=28, color=YELLOW)
        self.play(Write(assumption1_title))
        self.wait(1)

        assumption1_small = (
            Text("1. Continuity", font_size=20).to_edge(LEFT).shift(UP * 2.5)
        )
        self.play(Transform(assumption1_title, assumption1_small))
        assumptions_list.add(assumption1_title)

        # Assumption 2: Constant returns to scale
        assumption2_title = Text(
            "Assumption 2: Constant Returns", font_size=28, color=YELLOW
        )
        self.play(Write(assumption2_title))
        self.wait(1)

        eq1 = MathTex("2Y = F(2L, 2K)", font_size=48)
        self.play(Write(eq1))
        self.wait(2)

        # Island example
        self.play(FadeOut(eq1))
        self.island_example()

        # Generalize with lambda
        eq2 = MathTex(r"\lambda Y = F(\lambda L, \lambda K)", font_size=48)
        self.play(Write(eq2))
        self.wait(2)

        assumption2_small = (
            Text("2. Constant Returns", font_size=20).to_edge(LEFT).shift(UP * 2)
        )
        self.play(Transform(assumption2_title, assumption2_small), FadeOut(eq2))
        assumptions_list.add(assumption2_title)

        # Assumption 3: Diminishing marginal returns
        assumption3_title = Text(
            "Assumption 3: Diminishing Returns", font_size=28, color=YELLOW
        )
        self.play(Write(assumption3_title))
        self.wait(1)

        # Show derivatives
        derivs = MathTex(
            r"\frac{\partial F}{\partial L} > 0, \quad \frac{\partial F}{\partial K} > 0",
            font_size=40,
        )
        self.play(Write(derivs))
        self.wait(2)
        self.play(FadeOut(derivs))

        # Plot diminishing returns
        self.diminishing_returns_plot()

        assumption3_small = (
            Text("3. Diminishing Returns", font_size=20).to_edge(LEFT).shift(UP * 1.5)
        )
        self.play(Transform(assumption3_title, assumption3_small))
        assumptions_list.add(assumption3_title)

        self.wait(2)
        self.play(FadeOut(assumptions_list))

    def island_example(self):
        """Visual example with islands and factories"""
        # First island
        island1 = Circle(radius=1, color=GOLD, fill_opacity=0.3).shift(LEFT * 3)
        factory1 = Square(side_length=0.4, color=GRAY, fill_opacity=0.8).move_to(
            island1
        )
        workers1 = VGroup(
            *[
                Dot(radius=0.05, color=WHITE).move_to(
                    island1.get_center()
                    + np.array([0.3 * np.cos(i), 0.3 * np.sin(i), 0])
                )
                for i in range(5)
            ]
        )
        output1 = Text("100 🥥", font_size=24).next_to(island1, UP)

        self.play(Create(island1), Create(factory1), Create(workers1))
        self.play(Write(output1))
        self.wait(1)

        # Second island
        island2 = Circle(radius=1, color=GOLD, fill_opacity=0.3).shift(RIGHT * 3)
        factory2 = Square(side_length=0.4, color=GRAY, fill_opacity=0.8).move_to(
            island2
        )
        workers2 = VGroup(
            *[
                Dot(radius=0.05, color=WHITE).move_to(
                    island2.get_center()
                    + np.array([0.3 * np.cos(i), 0.3 * np.sin(i), 0])
                )
                for i in range(5)
            ]
        )
        output2 = Text("100 🥥", font_size=24).next_to(island2, UP)

        self.play(Create(island2), Create(factory2), Create(workers2))
        self.play(Write(output2))

        # Show total
        total = MathTex("100 + 100 = 200", font_size=36).to_edge(UP)
        self.play(Transform(VGroup(output1, output2), total))
        self.wait(2)

        self.play(
            FadeOut(
                island1,
                factory1,
                workers1,
                island2,
                factory2,
                workers2,
                output1,
                output2,
            )
        )

    def diminishing_returns_plot(self):
        """Plot showing diminishing marginal returns"""
        axes = Axes(
            x_range=[0, 10, 2],
            y_range=[0, 5, 1],
            x_length=8,
            y_length=5,
            axis_config={"include_numbers": True},
        )

        x_label = axes.get_x_axis_label("K", edge=DOWN)
        y_label = axes.get_y_axis_label("Y", edge=LEFT)

        # Cobb-Douglas like curve (square root for alpha=0.5)
        curve = axes.plot(lambda x: 2 * (x**0.4), color=BLUE, x_range=[0.1, 10])

        self.play(Create(axes), Write(x_label), Write(y_label))
        self.play(Create(curve))
        self.wait(2)

        # Show tangent lines at different points
        points = [1, 4, 8]
        for k in points:
            y_val = 2 * (k**0.4)
            slope = 2 * 0.4 * (k**-0.6)

            tangent = axes.plot(
                lambda x: y_val + slope * (x - k),
                color=RED,
                x_range=[max(0.1, k - 2), min(10, k + 2)],
            )
            dot = Dot(axes.c2p(k, y_val), color=RED)

            self.play(Create(tangent), FadeIn(dot))
            self.wait(1)
            if k != points[-1]:
                self.play(FadeOut(tangent, dot))

        self.wait(1)
        self.play(FadeOut(axes, x_label, y_label, curve, tangent, dot))

    def cobb_douglas(self):
        """Show Cobb-Douglas function"""
        cd_title = Text("Cobb-Douglas Production Function", font_size=36, color=YELLOW)
        cd_eq = MathTex(r"F(K, L) = K^\alpha L^{1-\alpha}", font_size=60)

        self.play(Write(cd_title))
        self.wait(1)
        self.play(cd_title.animate.to_edge(UP))
        self.play(Write(cd_eq))
        self.wait(3)

        # Firm's problem
        self.play(FadeOut(cd_title, cd_eq))

        firm_title = Text(
            "Firm's Profit Maximization", font_size=36, color=YELLOW
        ).to_edge(UP)
        profit_eq = MathTex(r"\max_{K, L} F(K, L) - rK - wL", font_size=48)

        self.play(Write(firm_title))
        self.play(Write(profit_eq))
        self.wait(2)

        result = MathTex("wL + rK = Y", font_size=48).shift(DOWN)
        self.play(Write(result))
        self.wait(2)

        # Euler's theorem
        euler_title = Text("Euler's Theorem", font_size=36, color=YELLOW).to_edge(UP)
        euler_eq = MathTex(
            r"g(L,K) = g_L(L,K) \cdot L + g_K(L,K) \cdot K", font_size=40
        )

        self.play(
            Transform(firm_title, euler_title),
            Transform(profit_eq, euler_eq),
            FadeOut(result),
        )
        self.wait(3)
        self.play(FadeOut(firm_title, profit_eq))

    def capital_accumulation(self):
        """Capital accumulation equation"""
        cap_title = Text("Capital Accumulation", font_size=36, color=YELLOW).to_edge(UP)
        self.play(Write(cap_title))

        cap_eq = MathTex(r"\dot{K} = sY - \delta K", font_size=60)
        self.play(Write(cap_eq))
        self.wait(3)

        explanation = (
            VGroup(
                MathTex(r"s = \text{savings rate}", font_size=32),
                MathTex(
                    r"\delta = \text{depreciation rate (}\approx 5\%\text{)}",
                    font_size=32,
                ),
            )
            .arrange(DOWN, aligned_edge=LEFT)
            .next_to(cap_eq, DOWN, buff=1)
        )

        self.play(Write(explanation))
        self.wait(3)
