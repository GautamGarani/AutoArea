from pyautocad import Autocad, APoint


def main():
    acad = Autocad(create_if_not_exists=True)
    print(f"Connected to document: {acad.doc.Name}")

    # Set the text height relative to your drawing size
    # If your area text is still small, increase this number (e.g., to 100 or 200)
    TEXT_HEIGHT = 100

    for obj in acad.iter_objects():
        if obj.ObjectName == "AcDbPolyline":

            # 1. Auto-Fix Open Polylines
            if not obj.Closed:
                obj.Closed = True

            area = obj.Area

            # --- CENTROID CALCULATION ---
            # Get all coordinates (returns a tuple like x1, y1, x2, y2...)
            coords = obj.Coordinates

            # Slice the list to get all X's (start at 0, step by 2)
            x_coords = coords[::2]
            # Slice the list to get all Y's (start at 1, step by 2)
            y_coords = coords[1::2]

            # Calculate the average (The Center)
            center_x = sum(x_coords) / len(x_coords)
            center_y = sum(y_coords) / len(y_coords)

            center_point = APoint(center_x, center_y)

            # --- CREATE CENTERED TEXT ---
            # We use AddText with the CORRECT order: (Point, Width, Text)
            # Width = 0 means the text box will auto-expand to fit the text
            text_string = f"{area:.2f}"
            mtext_obj = acad.model.AddText(center_point, 0, text_string)

            # Set Text Height
            mtext_obj.Height = TEXT_HEIGHT

            # Set Alignment to "Middle Center"
            # 1 = TopLeft, 5 = MiddleCenter (This is the magic number)
            mtext_obj.AttachmentPoint = 5

            # Color the polygon green
            obj.Color = 3
            print(f"Labeled polygon at {center_x:.2f}, {center_y:.2f}")

    print("Done! Check your drawing.")


if _name_ == "_main_":
    main()
