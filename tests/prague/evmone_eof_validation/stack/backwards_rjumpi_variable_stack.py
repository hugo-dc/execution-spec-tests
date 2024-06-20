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
                        0x01,
                        0x00,
                        0x04,
                        0x02,
                        0x00,
                        0x01,
                        0x00,
                        0x0e,
                        0x04,
                        0x00,
                        0x00,
                        0x00,
                        0x00,
                        0x80,
                        0x00,
                        0x04,
                        0x5f,
                        0x60,
                        0x00,
                        0xe1,
                        0x00,
                        0x02,
                        0x5f,
                        0x5f,
                        0x60,
                        0x00,
                        0xe1,
                        0xff,
                        0xfb,
                        0x00,

                     ]),
            ),
            "0xef0001010004020001000e04000000008000045f6000e100025f5f6000e1fffb00",
            None,
            id="backwards_rjumpi_variable_stack_0",
        ),
        pytest.param(
            Container(
                name="EOF1V00002",
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
                        0x10,
                        0x04,
                        0x00,
                        0x00,
                        0x00,
                        0x00,
                        0x80,
                        0x00,
                        0x04,
                        0x5f,
                        0x60,
                        0x00,
                        0xe1,
                        0x00,
                        0x02,
                        0x5f,
                        0x5f,
                        0x5f,
                        0x50,
                        0x60,
                        0x00,
                        0xe1,
                        0xff,
                        0xf9,
                        0x00,

                     ]),
            ),
            "0xef0001010004020001001004000000008000045f6000e100025f5f5f506000e1fff900",
            None,
            id="backwards_rjumpi_variable_stack_1",
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
                        0x15,
                        0x04,
                        0x00,
                        0x00,
                        0x00,
                        0x00,
                        0x80,
                        0x00,
                        0x04,
                        0x5f,
                        0x60,
                        0x00,
                        0xe1,
                        0x00,
                        0x02,
                        0x5f,
                        0x5f,
                        0x5f,
                        0x50,
                        0x60,
                        0x00,
                        0xe1,
                        0xff,
                        0xf9,
                        0x60,
                        0x00,
                        0xe1,
                        0xff,
                        0xf4,
                        0x00,

                     ]),
            ),
            "0xef0001010004020001001504000000008000045f6000e100025f5f5f506000e1fff96000e1fff400",
            None,
            id="backwards_rjumpi_variable_stack_2",
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
                        0x16,
                        0x04,
                        0x00,
                        0x00,
                        0x00,
                        0x00,
                        0x80,
                        0x00,
                        0x05,
                        0x5f,
                        0x60,
                        0x00,
                        0xe1,
                        0x00,
                        0x02,
                        0x5f,
                        0x5f,
                        0x5f,
                        0x50,
                        0x60,
                        0x00,
                        0xe1,
                        0xff,
                        0xf9,
                        0x5f,
                        0x60,
                        0x00,
                        0xe1,
                        0xff,
                        0xf3,
                        0x00,

                     ]),
            ),
            "0xef0001010004020001001604000000008000055f6000e100025f5f5f506000e1fff95f6000e1fff300",
            EOFException.INVALID_STACK_HEIGHT,
            id="backwards_rjumpi_variable_stack_3",
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
                        0x11,
                        0x04,
                        0x00,
                        0x00,
                        0x00,
                        0x00,
                        0x80,
                        0x00,
                        0x05,
                        0x5f,
                        0x60,
                        0x00,
                        0xe1,
                        0x00,
                        0x02,
                        0x5f,
                        0x5f,
                        0x5f,
                        0x60,
                        0x01,
                        0x01,
                        0x80,
                        0xe1,
                        0xff,
                        0xf9,
                        0x00,

                     ]),
            ),
            "0xef0001010004020001001104000000008000055f6000e100025f5f5f60010180e1fff900",
            None,
            id="backwards_rjumpi_variable_stack_4",
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
                        0x12,
                        0x04,
                        0x00,
                        0x00,
                        0x00,
                        0x00,
                        0x80,
                        0x00,
                        0x05,
                        0x5f,
                        0x60,
                        0x00,
                        0xe1,
                        0x00,
                        0x02,
                        0x5f,
                        0x5f,
                        0x5f,
                        0x60,
                        0x01,
                        0x01,
                        0x80,
                        0x80,
                        0xe1,
                        0xff,
                        0xf8,
                        0x00,

                     ]),
            ),
            "0xef0001010004020001001204000000008000055f6000e100025f5f5f6001018080e1fff800",
            EOFException.INVALID_STACK_HEIGHT,
            id="backwards_rjumpi_variable_stack_5",
        ),
        pytest.param(
            Container(
                name="EOF1V00007",
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
                        0x10,
                        0x04,
                        0x00,
                        0x00,
                        0x00,
                        0x00,
                        0x80,
                        0x00,
                        0x05,
                        0x5f,
                        0x60,
                        0x00,
                        0xe1,
                        0x00,
                        0x02,
                        0x5f,
                        0x5f,
                        0x5f,
                        0x5f,
                        0x5f,
                        0x50,
                        0xe1,
                        0xff,
                        0xfc,
                        0x00,

                     ]),
            ),
            "0xef0001010004020001001004000000008000055f6000e100025f5f5f5f5f50e1fffc00",
            EOFException.INVALID_STACK_HEIGHT,
            id="backwards_rjumpi_variable_stack_6",
        ),
        pytest.param(
            Container(
                name="EOF1V00008",
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
                        0x12,
                        0x04,
                        0x00,
                        0x00,
                        0x00,
                        0x00,
                        0x80,
                        0x00,
                        0x04,
                        0x5f,
                        0x60,
                        0x00,
                        0xe1,
                        0x00,
                        0x02,
                        0x5f,
                        0x5f,
                        0x5f,
                        0x50,
                        0x60,
                        0x00,
                        0xe1,
                        0xff,
                        0xf9,
                        0xe0,
                        0xff,
                        0xf6,

                     ]),
            ),
            "0xef0001010004020001001204000000008000045f6000e100025f5f5f506000e1fff9e0fff6",
            None,
            id="backwards_rjumpi_variable_stack_7",
        ),
        pytest.param(
            Container(
                name="EOF1V00009",
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
                        0x13,
                        0x04,
                        0x00,
                        0x00,
                        0x00,
                        0x00,
                        0x80,
                        0x00,
                        0x04,
                        0x5f,
                        0x60,
                        0x00,
                        0xe1,
                        0x00,
                        0x02,
                        0x5f,
                        0x5f,
                        0x5f,
                        0x50,
                        0x60,
                        0x00,
                        0xe1,
                        0xff,
                        0xf9,
                        0x5f,
                        0xe0,
                        0xff,
                        0xf5,

                     ]),
            ),
            "0xef0001010004020001001304000000008000045f6000e100025f5f5f506000e1fff95fe0fff5",
            EOFException.INVALID_STACK_HEIGHT,
            id="backwards_rjumpi_variable_stack_8",
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