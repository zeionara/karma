from .. import errors

def tokens_csrf(
    api,
    url,
    http_method,
    resolve_nosdc=False) -> dict:

    response = api(url, http_method)
    if (response.get("status") == 403) and (response.get("body") == "nosdc") and (resolve_nosdc):
        sdc_response = api.sdc()
        if sdc_response:
            return api.tokens.csrf()
        else:
            raise errors.CloudMailSdcGettingError(f"Received unexpected status code: {sdc_response.status_code}")
    else:
        return response

def tokens_download(
    api,
    url,
    http_method) -> dict:

    data = {
        "token": api.tokens.csrf(True)["body"]["token"]
    }

    return api(url, http_method, data=data)
