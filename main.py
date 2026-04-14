from scraper.scraper import get_books
from analysis.data_processing import process_books, generate_report
from database.database_manager import save_books

def run():
    try:
        books=get_books()
        df=process_books(books)
        save_books(df)
        generate_report(df)
        print("Running pipeline")
        
    except Exception as e:
        print("Erro:", e)
    
if __name__=="__main__":
    run()