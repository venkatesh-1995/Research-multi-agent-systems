# from src.tools.tools import web_search,scrape_url


# # web_search_result = web_search.invoke(
# #     {"query": "latest news on AI?"}
# # )
# # print(web_search_result)


# scrape_result = scrape_url.invoke(
#     {"url": "https://guides.library.georgetown.edu/ai/news"}
# )
# print(scrape_result)



from src.pipeline.pipeline import research_pipeline

topic="the impact of ai on the job market in 2026?"

research_pipeline(topic) 
