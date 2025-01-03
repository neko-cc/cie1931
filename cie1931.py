import matplotlib.pyplot as plt
import colour.plotting as colour_plotting

# Define RGB coordinates
r_xy = (0.68, 0.31)
g_xy = (0.21, 0.65)
b_xy = (0.15, 0.06)

def plot_cie1931_with_triangle(triangle_coords):
    # Create a new figure
    fig, ax = plt.subplots(figsize=(8, 6))

    # Plot the CIE 1931 Chromaticity Diagram using colour-science
    colour_plotting.plot_chromaticity_diagram_CIE1931(standalone=False, axes=ax)

    # Extract x and y coordinates from triangle_coords
    x_coords = [coord[0] for coord in triangle_coords]
    y_coords = [coord[1] for coord in triangle_coords]

    # Close the triangle by repeating the first point at the end
    x_coords.append(x_coords[0])
    y_coords.append(y_coords[0])

    # Plot the triangle
    ax.plot(x_coords, y_coords, color='black', lw=2, label='Triangle')

    # Set labels and title
    ax.set_xlabel('x')
    ax.set_ylabel('y')
    ax.set_title('CIE 1931 Chromaticity Diagram with Triangle')

    # Add legend
    ax.legend()

    # Function to handle zooming with mouse wheel
    def on_scroll(event):
        base_scale = 1.1
        scale_factor = base_scale if event.button == 'up' else 1 / base_scale

        # Get current view limits
        x_min, x_max = ax.get_xlim()
        y_min, y_max = ax.get_ylim()

        # Calculate new view limits
        x_center = (x_min + x_max) / 2
        y_center = (y_min + y_max) / 2

        new_x_min = x_center - (x_center - x_min) * scale_factor
        new_x_max = x_center + (x_max - x_center) * scale_factor
        new_y_min = y_center - (y_center - y_min) * scale_factor
        new_y_max = y_center + (y_max - y_center) * scale_factor

        # Set new view limits
        ax.set_xlim(new_x_min, new_x_max)
        ax.set_ylim(new_y_min, new_y_max)
        fig.canvas.draw_idle()

    # Function to handle mouse button press
    def on_press(event):
        if event.button == 1:  # Left mouse button
            ax.press = (event.xdata, event.ydata)

    # Function to handle mouse motion
    def on_motion(event):
        if event.button == 1 and hasattr(ax, 'press'):
            x0, y0 = ax.press
            dx = event.xdata - x0
            dy = event.ydata - y0
            x_min, x_max = ax.get_xlim()
            y_min, y_max = ax.get_ylim()
            ax.set_xlim(x_min - dx, x_max - dx)
            ax.set_ylim(y_min - dy, y_max - dy)
            fig.canvas.draw_idle()

    # Function to handle mouse button release
    def on_release(event):
        if hasattr(ax, 'press'):
            del ax.press
            fig.canvas.draw_idle()

    # Function to handle click events
    def on_click(event):
        if event.button == 1:  # Left mouse button
            x, y = event.xdata, event.ydata
            print(f"Clicked at coordinates: ({x:.4f}, {y:.4f})")

    # Plot the D65 point
    d65_x, d65_y = 0.3127, 0.3290
    ax.plot(d65_x, d65_y, 'ko', markersize=5)  # Black dot
    ax.text(d65_x, d65_y, 'D65', fontsize=10, color='black', ha='right', va='bottom')

    # Connect the scroll event to the handler function
    fig.canvas.mpl_connect('scroll_event', on_scroll)

    # Connect the mouse press event to the handler function
    fig.canvas.mpl_connect('button_press_event', on_press)

    # Connect the mouse motion event to the handler function
    fig.canvas.mpl_connect('motion_notify_event', on_motion)

    # Connect the mouse release event to the handler function
    fig.canvas.mpl_connect('button_release_event', on_release)

    # Connect the click event to the handler function
    fig.canvas.mpl_connect('button_press_event', on_click)

    # Show the plot
    plt.show()

if __name__ == "__main__":
    # Example triangle coordinates
    triangle_coords = [r_xy, g_xy, b_xy]
    plot_cie1931_with_triangle(triangle_coords)