def convert_to_format(space_filler: str, symbol: str, key: str | int,
                      value) -> list[str]:
    if isinstance(value, str):
        value = f'{value}' if len(value) == 0 else value
    return [''.join([space_filler, f' {symbol}', f' {key}:', f' {value}']
                    ).rstrip(' ')]
