def convert_to_format(space_filler: str, symbol: str, key: str | int,
                      value) -> list[str]:
    return [''.join([space_filler, f' {symbol}', f' {key}:', f' {value}']
                    )]
