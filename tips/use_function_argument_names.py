from my_pipeline.apis import fetch_weather_forecast


# don't do this
fetch_weather_forecast('London', 5, True, 3)

# do this instead
fetch_weather_forecast('London', days=5, retry=True, num_retries=3)