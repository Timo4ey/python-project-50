def convert_to_format(space_feeler: str, symbol: str, key: str | int,
                      value) -> list[str]:
    return [''.join([space_feeler, f' {symbol}', f' {key}:', f' {value}']
                    ).rstrip(' ')]
