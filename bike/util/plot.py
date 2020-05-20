import plotly.graph_objects as go
import plotly.io as pio
import plotly.offline as pyo

from bike.stats import BatchStats


class Plot:

    def __init__(
        self,
        image_width: int = 1200,
        image_height: int = 900
    ) -> None:

        self.IMAGE_WIDTH = image_width
        self.IMAGE_HEIGHT = image_height

        pyo.init_notebook_mode(connected=False)
        pio.renderers.default = 'notebook'

    def ga_convergence(
        self,
        batch_stats: BatchStats,
        filename: str = 'ga-convergence'
    ):
        fig = go.Figure()

        fig.add_trace(
            go.Scatter(
                y=batch_stats.avg_fitness,
                mode='lines',
                name='avg'
            )
        )

        fig.add_trace(
            go.Scatter(
                y=batch_stats.min_fitness,
                mode='lines',
                name='min'
            )
        )

        fig.add_trace(
            go.Scatter(
                y=batch_stats.max_fitness,
                mode='lines',
                name='max'
            )
        )

        fig.update_layout(
            xaxis_title='Epochs',
            yaxis_title='Fitness'
        )

        pyo.iplot(
            fig,
            filename=filename,
            image_width=self.IMAGE_WIDTH,
            image_height=self.IMAGE_HEIGHT
        )
