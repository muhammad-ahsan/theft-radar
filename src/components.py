from abc import ABC, abstractmethod
import streamlit as st

from src.utils import load_data


class IComponent(ABC):
    def __init__(self, **kwargs):
        self.kwargs = kwargs

    @abstractmethod
    def setup(self):
        ...


class Header(IComponent):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def setup(self):
        st.header("Bike Theft Radar!")

        # """
        # Theft period is from January 2021 to May 2022. The exact geo coordinates are approximated using the
        # information from [data source](https://www.govdata.de/web/guest/suchen/-/details/fahrraddiebstahl-in-berlin).
        # The next enhancement will include the deep learning based prediction model to predict geo-coordinates where theft
        # incident is about to occur.
        # """


class Body(IComponent):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def setup(self):
        selected_option = st.selectbox(
            "Select City", ("Berlin", "Los Angeles")
        )

        data_path: str = ""
        if selected_option == "Berlin":
            data_path = "data/bicycle_theft_berlin.csv"
        elif selected_option == "Los Angeles":
            raise NotImplementedError("Not implemented yet")
        "#### Number of samples"
        samples = st.slider("", min_value=100, max_value=25000)

        data = load_data(data_path, samples)

        "#### Theft Map"
        st.map(data)
        checked = st.checkbox("Show raw data")

        if checked:
            "#### Source Data"
            st.dataframe(data)
            st.subheader("About Dataset")

            st.markdown("""Theft period is from January 2021 to May 2022. The exact geo coordinates are approximated using the
            information from [data source](https://www.govdata.de/web/guest/suchen/-/details/fahrraddiebstahl-in-berlin).
            The next enhancement will include the deep learning based prediction model to predict geo-coordinates where theft
            incident is about to occur""")


class Footer(IComponent):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)

    def setup(self, **kwargs):
        st.subheader("Contact Developer")
        st.markdown("Programmed with ❤️ by [Muhammad Ahsan](https://www.linkedin.com/in/muhammad-ahsan/)")
