# LTBI Data Visualization Dashboard

## Introduction

**LTBI Data Visualization Dashboard** is an interactive web application designed to visualize and explore latent tuberculosis infection (LTBI) data across different countries and regions. Built with **HTML5**, **CSS3**, and [**D3.js (v7)**](https://d3js.org/), the dashboard offers a comprehensive suite of interactive visualizations. It enables users to gain insights into LTBI metrics, examine relationships, and observe trends over time.

---

## Project Documentation

### Design Choices

#### Visual Design

- **Color Schemes:**  
  The dashboard uses a consistent color palette centered around blues, creating a professional and cohesive aesthetic. Custom color schemes like `interpolateBlues` and `interpolateLightBlue` are used to differentiate data categories and enhance visual clarity.

- **Typography:**  
  Fonts such as **Inter** and **Segoe UI** are chosen for their modern appearance and high readability.

- **Layout and Styling:**  
  A responsive grid layout (`display: grid`) organizes the dashboard sections. Each visualization is placed within a `.section` class, styled with modern gradients, rounded corners, and subtle shadows for visual appeal.

#### User Interface

- **Responsive Design:**  
  The dashboard adjusts seamlessly to different screen sizes using media queries and flexible grid layouts.

- **Controls and Filters:**  
  Interactive controls, including dropdown menus and file inputs, allow users to filter data based on metrics, relationships, countries, and years. These controls are designed for consistency and usability.

- **Navigation and Legends:**  
  The inclusion of interactive legends and breadcrumb trails enhances user navigation and improves overall comprehension of the visualizations.

#### Interactivity

- **Hover Effects:**  
  Tooltips reveal detailed information when hovering over data points, enhancing exploration.

- **Click Events:**  
  Clicking on data elements triggers selections that update all visualizations, enabling cross-filtering.

- **Zooming and Panning:**  
  Visualizations such as dynamic graphs and choropleth maps support zoom and pan interactions to allow detailed data examination.

---

### Data Preprocessing

- **Data Sources:**
  - **Primary Dataset:**  
    Uses `processed_LTBI_dataset.csv`, which includes LTBI metrics for various countries over multiple years.
  - **Geospatial Data:**  
    World geographical data is fetched from an external GeoJSON source for the choropleth map.

- **Preprocessing Steps:**
  - **Data Parsing:**  
    CSV data is parsed using D3 functions, ensuring numerical fields are correctly converted.
  - **Hierarchical Structuring:**  
    Data is grouped and nested (based on regions, subregions, and countries) for hierarchical visualizations like the sunburst chart and treemap.
  - **Metric Calculations:**  
    Aggregations (sums, averages, etc.) are computed as required.

---

### Visualizations

#### 1. Dynamic Graph with Filters

- **Description:**  
  A force-directed graph where each node represents a country, connected by selected relationship types (e.g., WHO Region, Income Level).

- **Interactive Features:**
  - **Node Size Adjustment:**  
    Users can choose a metric (e.g., Average Household Size) to determine node sizes.
  - **Relationship Filters:**  
    Options enable users to switch between relationship types (such as Region or Sub-region).
  - **Hover Tooltips:**  
    Display detailed information on nodes and connections upon hover.
  - **Click Events:**  
    Selecting a node highlights it and synchronizes updates with other visualizations.
  - **Zoom and Pan:**  
    Facilitates detailed examination of the graph.
  - **Legend Interaction:**  
    An interactive legend allows toggling the visibility of nodes by region.

- **Implementation Details:**
  - Utilizes D3's force simulation (`d3.forceSimulation`) for positioning nodes.
  - Implements drag behavior using `d3.drag()`.
  - Edges are colored using a categorical color scale based on relationship types.
  - User settings are preserved in `localStorage` for state persistence.
  - Graphs can be exported as SVG files via an export functionality.

---

#### 2. Interactive Choropleth Map

- **Description:**  
  A world map that visualizes LTBI metrics per country. Each country is shaded based on the data for a selected year.

- **Interactive Features:**
  - **Year Selection:**  
    Users choose the year to display corresponding data.
  - **Hover Tooltips:**  
    Country names and metric values are revealed on hover.
  - **Click Events:**  
    Clicking a country zooms into it and selects it for cross-filtering.
  - **Zoom and Pan:**  
    Enables smooth and detailed navigation across the map.

- **Implementation Details:**
  - Uses the `geoNaturalEarth1` projection for realistic map rendering.
  - Applies a sequential color scale using an interpolated blues scheme via `d3.scaleSequential`.
  - GeoJSON features are bound to CSV data using ISO country codes.
  - A dynamic legend updates with the selected year’s data.

---

#### 3. Interactive Sunburst Chart

- **Description:**  
  A hierarchical sunburst chart presenting the distribution of LTBI metrics across countries and years.

- **Interactive Features:**
  - **Country Filter:**  
    Allows users to filter the chart by selecting specific countries or viewing all data.
  - **Color Scheme Selection:**  
    Users can select different color schemes for better data differentiation.
  - **Hover Tooltips:**  
    Display detailed segment information on hover.
  - **Click Events:**  
    Clicking a segment updates the breadcrumb trail and can trigger country selection.

- **Implementation Details:**
  - Data is structured hierarchically with a root node, countries, and years.
  - D3's partition layout computes sizes and arc positions.
  - Arcs are generated via `d3.arc()` with smooth transitions.
  - Includes an interactive breadcrumb trail that traces the navigation path within the hierarchy.

---

#### 4. Bar Chart Timeline Visualization

- **Description:**  
  A bar chart presenting LTBI metrics over time, allowing comparisons across selected countries and metrics.

- **Interactive Features:**
  - **Country and Metric Filters:**  
    Users can select specific countries and metrics for display.
  - **Hover Tooltips:**  
    Detailed information for each bar (e.g., metric value for a specific year) is provided on hover.
  - **Click Events:**  
    Clicking on a bar can select a country, triggering updates in other visualizations.
  - **Sorting:**  
    Data is sorted by the selected metric for improved clarity.

- **Implementation Details:**
  - Uses a band scale for the X-axis (years) and a linear scale for the Y-axis (metric values).
  - Bars are colored with a predefined blue color scheme.
  - Axes feature appropriate tick formatting for readability.
  - Implements data validation to handle any missing or invalid data.

---

#### 5. Hierarchical Treemap

- **Description:**  
  A treemap visualization representing hierarchical data (regions, subregions, and countries) with support for custom dataset uploads.

- **Interactive Features:**
  - **File Upload:**  
    Users can upload their own CSV or TSV files to generate a custom treemap.
  - **Hover Tooltips:**  
    Each cell displays metadata and metric values on hover.
  - **Click Events:**  
    Clicking on a cell selects the corresponding country, which then updates other visualizations.
  - **Responsive Layout:**  
    The treemap dynamically adjusts to window size changes.

- **Implementation Details:**
  - Uploaded files are parsed with `d3.csvParse` or `d3.tsvParse` based on the file extension.
  - Data is structured into a hierarchy using fields like 'Region', 'Sub-region', and 'Country'.
  - D3’s treemap layout calculates cell sizes and positions.
  - Cells are colored by their parent region using the blue color scheme.
  - Dynamic text labels are added to cells and are hidden if they do not fit within cell dimensions.

---

### Advanced Features

#### Cross-Filtering and State Persistence

- **Country Selection:**  
  Selecting a country in any visualization updates all others to reflect that choice.

- **Event Handling:**  
  Custom events are dispatched and listened to across components to maintain a consistent state.

- **Local Storage:**  
  User preferences and selections are saved using `localStorage`, ensuring state is preserved across sessions.

#### Export Functionality

- **Graph Export:**  
  The dynamic graph can be exported as an SVG file. This process involves serializing the SVG content into a Blob and generating a temporary download link.

#### User Data Upload

- **Custom Data:**  
  Users can upload custom datasets through the treemap visualization, enhancing the dashboard's flexibility.

- **Error Handling:**  
  Robust error handling ensures that users are informed if their uploaded data cannot be processed.

---

## Conclusion

The **LTBI Data Visualization Dashboard** provides a robust, interactive platform for exploring latent tuberculosis infection data. By integrating diverse visualization types and advanced interactive features, users can gain deep insights into LTBI metrics. The design emphasizes both usability and visual appeal, while the codebase remains organized for maintainability and future enhancements.


