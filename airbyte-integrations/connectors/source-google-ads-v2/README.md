# Google Ads V2 Source

This is a manifest-only connector for Google Ads, built using the Airbyte low-code CDK (declarative manifest). It uses the [Google Ads API v22](https://developers.google.com/google-ads/api/docs/start) via GAQL (Google Ads Query Language).

## Streams

### Full-refresh streams
| Stream | Description |
|---|---|
| `customers` | Accessible customer accounts (via `listAccessibleCustomers`) |
| `customer` | Customer account details |
| `campaigns` | All campaigns in the account |
| `ad_groups` | All ad groups across campaigns |
| `ads` | All ads across ad groups |
| `keywords` | Keywords for search campaigns |
| `conversion_actions` | Conversion action configurations |
| `labels` | Account labels |

### Incremental streams
| Stream | Cursor field | Description |
|---|---|---|
| `campaign_performance` | `segments.date` | Daily campaign performance metrics |
| `ad_group_performance` | `segments.date` | Daily ad group performance metrics |
| `keyword_performance` | `segments.date` | Daily keyword performance metrics |
| `search_terms_report` | `segments.date` | Search terms that triggered ads |
| `geographic_performance` | `segments.date` | Performance by geographic location |
| `audience_performance` | `segments.date` | Performance by audience segment |
| `click_performance` | `segments.date` | Individual click data |

## Configuration

| Parameter | Required | Description |
|---|---|---|
| `developer_token` | Yes | Google Ads API developer token |
| `customer_id` | Yes | Google Ads customer ID (10 digits, with or without hyphens) |
| `login_customer_id` | No | Manager account customer ID (if accessing via manager account) |
| `credentials.client_id` | Yes | OAuth client ID |
| `credentials.client_secret` | Yes | OAuth client secret |
| `credentials.refresh_token` | Yes | OAuth refresh token |
| `start_date` | Yes | Start date for incremental streams (YYYY-MM-DD) |
| `end_date` | No | End date for incremental streams (YYYY-MM-DD) |
| `custom_queries` | No | Additional GAQL queries to create custom streams |

## Build

```bash
airbyte-ci connectors --name=source-google-ads-v2 build
```

## Test

```bash
airbyte-ci connectors --name=source-google-ads-v2 test
```
