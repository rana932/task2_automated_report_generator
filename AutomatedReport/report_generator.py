import csv
from fpdf import FPDF


# Function to read data from CSV and analyze it
def read_and_analyze_data(file_path):
    data = []
    total_sales = {}

    # Read the CSV file
    with open(file_path, 'r') as file:
        csv_reader = csv.DictReader(file)
        for row in csv_reader:
            product = str(row['Product'])
            quantity = int(row['Quantity'])
            price = float(row['Price'])
            sale_total = quantity * price

            # Store data
            data.append({
                'Date': row['Date'],
                'Product': product,
                'Quantity': quantity,
                'Price': price,
                'Total Sale': sale_total
            })

            # Aggregate total sales by product
            if product not in total_sales:
                total_sales[product] = 0
            total_sales[product] += sale_total

    return data, total_sales


# Function to generate the PDF report
def generate_pdf(data, total_sales, output_path):
    pdf = FPDF()
    pdf.add_page()  # Added missing page creation
    pdf.set_auto_page_break(auto=True, margin=15)

    # Add title
    pdf.set_font('Arial', 'B', 16)
    pdf.cell(200, 10, 'Sales Report', ln=True, align='C')

    # Add a table for detailed data
    pdf.ln(10)
    pdf.set_font('Arial', 'B', 12)

    # Column headers
    pdf.cell(40, 10, 'Date', border=1)
    pdf.cell(50, 10, 'Product', border=1)
    pdf.cell(30, 10, 'Quantity', border=1)
    pdf.cell(30, 10, 'Price', border=1)
    pdf.cell(40, 10, 'Total Sale', border=1)
    pdf.ln()

    # Data rows
    pdf.set_font('Arial', '', 12)
    for row in data:
        pdf.cell(40, 10, row['Date'], border=1)
        pdf.cell(50, 10, row['Product'], border=1)
        pdf.cell(30, 10, str(row['Quantity']), border=1)
        pdf.cell(30, 10, f"${row['Price']:.2f}", border=1)
        pdf.cell(40, 10, f"${row['Total Sale']:.2f}", border=1)
        pdf.ln()

    # Add Summary of total sales by product
    pdf.ln(10)
    pdf.set_font('Arial', 'B', 12)
    pdf.cell(40, 10, 'Product', border=1)
    pdf.cell(40, 10, 'Total Sales', border=1)
    pdf.ln()

    pdf.set_font('Arial', '', 12)
    for product, total in total_sales.items():
        pdf.cell(40, 10, product, border=1)
        pdf.cell(40, 10, f"${total:.2f}", border=1)
        pdf.ln()

    # Output the PDF
    pdf.output(output_path)


# Main function to execute the script
def main():
    input_file = 'data.csv'  # Path to input CSV file
    output_file = 'sales_report.pdf'  # Path to PDF report

    # Read and analyze the data
    data, total_sales = read_and_analyze_data(input_file)

    # Generate the PDF report
    generate_pdf(data, total_sales, output_file)
    print(f"Report Generated: {output_file}")


if __name__ == "__main__":
    main()