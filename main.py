from fpdf import FPDF
from modules.report import graph

def export_report_to_pdf(report: str, file_name: str) -> None:
    """
    Export a report to a PDF file.

    Args:
        report (str): The content of the report to be exported.
        file_name (str): The name of the output PDF file.
    """
    # Initialize the PDF object
    pdf = FPDF()
    pdf.set_auto_page_break(auto=True, margin=15)
    pdf.add_page()
    pdf.set_font("Arial", size=12)

    # Add report content to the PDF
    for line in report.split('\n'):  # Split report into lines for PDF formatting
        pdf.multi_cell(0, 10, line)  # multi_cell wraps text automatically

    # Save the PDF
    pdf.output(file_name)
    print(f"Report exported successfully to {file_name}")

max_analysts = 1
topic = "Main us stock market news for 5 Jan 2025 and expectations for Jan 6 2025"
thread = {"configurable": {"thread_id": "4"}}

for event in graph.stream({"topic":topic,
                           "max_analysts":max_analysts}, 
                          thread, 
                          stream_mode="values"):
    
    analysts = event.get('analysts', '')
    if analysts:
        for analyst in analysts:
            print(f"Name: {analyst.name}")
            print(f"Affiliation: {analyst.affiliation}")
            print(f"Role: {analyst.role}")
            print(f"Description: {analyst.description}")
            print("-" * 50)  

human_feedback = None
graph.update_state(thread, {"human_analyst_feedback": 
                            human_feedback}, as_node="human_feedback")

for event in graph.stream(None, thread, stream_mode="updates"):
    print("--Node--")
    node_name = next(iter(event.keys()))
    print(node_name)

final_state = graph.get_state(thread)
report = final_state.values.get('final_report')
export_report_to_pdf(report, 'final_report.pdf')