
# General rules
- [ ] Commit your changes to a public repository in GitHub.
- [x] Add a README.md with instructions to run the code.

# Support the following endpoint
GET /allBerryStats

Response:

```json
{
    "berries_names": [...],
    "min_growth_time": "" // time, int
    "median_growth_time": "", // time, float
    "max_growth_time": "" // time, int
    "variance_growth_time": "" // time, float
    "mean_growth_time": "", // time, float
    "frequency_growth_time": "", // time, {growth_time: frequency, ...}
}
```

This endpoint should consume an external API to get the proper info, here is the documentation page: https://pokeapi.co/docs/v2#berries

- [x] The data must be human-readable.
- [x] Use environment variables for configuration.
- [x] The response must include the content-type header (application/json)
- [x] Functions must be tested with pytest.

For extra points:
- [ ] Upload and deploy the solution to a free cloud service for example python anywhere or equivalent.
- [x] Use a containering system like docker
- [ ] Use a cache to speed up the queries.
- [x] Use a Python library (example: Matplotlib) to create a Histogram graph and display the image in a plain html.
