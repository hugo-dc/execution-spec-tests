"""
EOF v1 validation code
"""

import pytest
from ethereum_test_tools import EOFTestFiller
from ethereum_test_tools.eof.v1 import Container, EOFException

@pytest.mark.parametrize(
    "eof_code,expected_hex_bytecode,exception",
    [
        pytest.param(
            Container(
                name="EOF1V00001",
                raw_bytes=bytes(
                     [
                        0xef,
                        0x00,
                        0x01,
                        0x05,
                        0x00,
                        0x01,
                        0x00,
                        0xfe,

                     ]),
            ),
            "0xef000105000100fe",
            EOFException.MISSING_TYPE_HEADER,
            id="EOF1_unknown_section_0",
        ),
        pytest.param(
            Container(
                name="EOF1V00002",
                raw_bytes=bytes(
                     [
                        0xef,
                        0x00,
                        0x01,
                        0xff,
                        0x00,
                        0x01,
                        0x00,
                        0xfe,

                     ]),
            ),
            "0xef0001ff000100fe",
            EOFException.MISSING_TYPE_HEADER,
            id="EOF1_unknown_section_1",
        ),
        pytest.param(
            Container(
                name="EOF1V00003",
                raw_bytes=bytes(
                     [
                        0xef,
                        0x00,
                        0x01,
                        0x01,
                        0x00,
                        0x04,
                        0x02,
                        0x00,
                        0x01,
                        0x00,
                        0x01,
                        0x05,
                        0x00,
                        0x01,
                        0x00,
                        0x00,
                        0x80,
                        0x00,
                        0x00,
                        0xfe,
                        0x00,

                     ]),
            ),
            "0xef000101000402000100010500010000800000fe00",
            EOFException.MISSING_DATA_SECTION,
            id="EOF1_unknown_section_2",
        ),
        pytest.param(
            Container(
                name="EOF1V00004",
                raw_bytes=bytes(
                     [
                        0xef,
                        0x00,
                        0x01,
                        0x01,
                        0x00,
                        0x04,
                        0x02,
                        0x00,
                        0x01,
                        0x00,
                        0x01,
                        0xff,
                        0x00,
                        0x01,
                        0x00,
                        0x00,
                        0x80,
                        0x00,
                        0x00,
                        0xfe,
                        0x00,

                     ]),
            ),
            "0xef00010100040200010001ff00010000800000fe00",
            EOFException.MISSING_DATA_SECTION,
            id="EOF1_unknown_section_3",
        ),
        pytest.param(
            Container(
                name="EOF1V00005",
                raw_bytes=bytes(
                     [
                        0xef,
                        0x00,
                        0x01,
                        0x01,
                        0x00,
                        0x04,
                        0x02,
                        0x00,
                        0x01,
                        0x00,
                        0x01,
                        0x04,
                        0x00,
                        0x01,
                        0x05,
                        0x00,
                        0x01,
                        0x00,
                        0x00,
                        0x80,
                        0x00,
                        0x00,
                        0xfe,
                        0xaa,
                        0x00,

                     ]),
            ),
            "0xef000101000402000100010400010500010000800000feaa00",
            EOFException.MISSING_TERMINATOR,
            id="EOF1_unknown_section_4",
        ),
        pytest.param(
            Container(
                name="EOF1V00006",
                raw_bytes=bytes(
                     [
                        0xef,
                        0x00,
                        0x01,
                        0x01,
                        0x00,
                        0x04,
                        0x02,
                        0x00,
                        0x01,
                        0x00,
                        0x01,
                        0x04,
                        0x00,
                        0x01,
                        0xff,
                        0x00,
                        0x01,
                        0x00,
                        0x00,
                        0x80,
                        0x00,
                        0x00,
                        0xfe,
                        0xaa,
                        0x00,

                     ]),
            ),
            "0xef00010100040200010001040001ff00010000800000feaa00",
            EOFException.MISSING_TERMINATOR,
            id="EOF1_unknown_section_5",
        ),
        
    ]
)

def test_example_valid_invalid(
    eof_test: EOFTestFiller,
    eof_code: Container,
    expected_hex_bytecode: str,
    exception: EOFException | None,
):
    """
    Verify eof container construction and exception
    """
    if expected_hex_bytecode[0:2] == "0x":
        expected_hex_bytecode = expected_hex_bytecode[2:]
    assert bytes(eof_code) == bytes.fromhex(expected_hex_bytecode)

    eof_test(
        data=eof_code,
        expect_exception=exception,
    )