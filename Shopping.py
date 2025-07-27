from agents import Agent
from main import config
import requests

def run_agent():
    url = "https://template-03-api.vercel.app/api/products"
    response = requests.get(url)
    
    if response.status_code != 200:
        return "Failed to fetch products."
    
    data = response.json()
    products = data.get("data", [])
    
    if not products:
        return "No products found."
    
    result = "\n".join(
        f"{product['productName']} - Rs.{product['price']}"
        for product in products
    )
    return result

if __name__ == "__main__":
    print(run_agent())



# from agents import Agent, function_tool, Runner
# from main import config
# import requests

# # Tool: Get all products under a given price
# @function_tool
# def get_products_under_price(price: float = 500) -> str:
#     url = f"https://template-03-api.vercel.app/api/products"
#     response = requests.get(url)

#     if response.status_code == 200:
#         print(response.text)
#         data = response.json()
#         filtered = [p for p in data if p['price'] <= price]
#         result = "\n".join([f"{p['title']} - Rs.{p['price']}" for p in filtered])
#         return result if result else "No products found under this price."
#     else:
#         return "Failed to fetch products."

# # Agent Setup
# agent = Agent(
#     name="Shopping Agent",
#     instructions="You are a helpful shopping assistant. Answer questions about products under a certain price.",
#     tools=[get_products_under_price]
# )

# # Run the agent with user input
# response = Runner.run_sync(
#     agent,
#     input="show me all products under price 500",
#     run_config=config
# )

# # Output
# print("\n🛒 Final Output:\n")
# print(response.final_output)



# # Tool: Get all products under a given price
# @function_tool
# def get_products_under_price(price: float = 500.0) -> str:
#     url = "https://template-03-api.vercel.app/api/products"
#     response = requests.get(url)

#     if response.status_code == 200:
#         data = response.json()
#         filtered = [p for p in data if p['price'] <= price]
#         result = "\n".join([f"{p['title']} - Rs.{p['price']}" for p in filtered])
#         return result if result else "No products found under this price."
#     else:
#         return "Failed to fetch products."

# # Agent Setup
# agent = Agent(
#     name="Shopping Agent",
#     instructions="You are a helpful shopping assistant. Answer questions about products under a certain price.",
#     tools=[get_products_under_price]
# )

# # Run the agent with user input
# response = Runner.run_sync(
#     agent,
#     input="get_products_under_price(500)",
#     run_config=config
# )

# # Output
# print("\n🛒 Final Output:\n")
# print(response.final_output)


