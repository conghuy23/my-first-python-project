#============ PHẦN 1: LIST & LIST COMPREHENSION ============#
class PortfolioAnalyzer:
    """Phân tích danh mục đàu tư sử dụng list"""
    
    def __init__(self):
        self.portfolio = []
        self.transactions =[]
        self.price_history =[]

#1.1.LIST -  danh sách cổ phiếu
    def initialize(self):
        """Khởi tạo danh mục với List"""
        # danh sách cổ phiếu (list of tuples)
        self.portfolio = [
        ("VIC", "Vingroup", 1000, 4500, "VN30"),
        ("VNM", "Vinamilk", 500, 120000, "VN30"),
        ("FPT", "FPT Corporation", 200, 40000, "VN30"),
        ("MSN", "Masan Group", 300, 90000, "VN30"),
        ("GAS", "PetroVietnam Gas", 150, 110000, "VN30"),
        ("HPG", "Hoa Phat Group", 400, 30000, "VN30")

    ]

        print (" danh mục đầu tư :")
        for i,  stock in enumerate(self.porfolio, 1):
          symbol, name, quantity, price, index = stock
        print(f"{i}. {symbol}: {name} - {quantity:,} cp @ {price:,.0f} VND")

#1.2. LIST COMPREHENSION - tính toán nhannh 
        def calculate_portfolio_stats(self):
         """ tính toán thống kê danh mục với list comprehension"""
         #a, tính giá trị từng vị thế 
         positon_values = [quantity * price 
                      for symbol,  name, quantity, price, index in self.portfolio] 
    
    
    
    
    