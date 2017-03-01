# python version 1.0						DO NOT EDIT
#
# Generated by smidump version 0.4.8:
#
#   smidump -f python COMETMS-MIB

FILENAME = "ms.mib"

MIB = {
    "moduleName" : "COMETMS-MIB",

    "COMETMS-MIB" : {
        "nodetype" : "module",
        "language" : "SMIv1",
    },

    "imports" : (
        {"module" : "RFC1155-SMI", "name" : "enterprises"},
        {"module" : "RFC1155-SMI", "name" : "IpAddress"},
        {"module" : "RFC1155-SMI", "name" : "Counter"},
        {"module" : "RFC1155-SMI", "name" : "TimeTicks"},
        {"module" : "RFC-1212", "name" : "OBJECT-TYPE"},
        {"module" : "RFC1213-MIB", "name" : "DisplayString"},
    ),

    "nodes" : {
        "comet" : {
            "nodetype" : "node",
            "moduleName" : "COMETMS-MIB",
            "oid" : "1.3.6.1.4.1.22626",
        }, # node
        "products" : {
            "nodetype" : "node",
            "moduleName" : "COMETMS-MIB",
            "oid" : "1.3.6.1.4.1.22626.1",
        }, # node
        "ms" : {
            "nodetype" : "node",
            "moduleName" : "COMETMS-MIB",
            "oid" : "1.3.6.1.4.1.22626.1.4",
        }, # node
        "settings" : {
            "nodetype" : "node",
            "moduleName" : "COMETMS-MIB",
            "oid" : "1.3.6.1.4.1.22626.1.4.1",
        }, # node
        "messageString" : {
            "nodetype" : "scalar",
            "moduleName" : "COMETMS-MIB",
            "oid" : "1.3.6.1.4.1.22626.1.4.1.1",
            "status" : "current",
            "syntax" : {
                "type" :                 {
                    "basetype" : "OctetString",
                    "parent module" : {
                        "name" : "RFC1213-MIB",
                        "type" : "DisplayString",
                    },
                    "ranges" : [
                    {
                        "min" : "0",
                        "max" : "128"
                    },
                    ],
                    "range" : {
                        "min" : "0",
                        "max" : "128"
                    },
                },
            },
            "access" : "readonly",
            "description" :
                """Message giving more detailed information on alarms""",
        }, # scalar
        "msName" : {
            "nodetype" : "scalar",
            "moduleName" : "COMETMS-MIB",
            "oid" : "1.3.6.1.4.1.22626.1.4.1.2",
            "status" : "current",
            "syntax" : {
                "type" :                 {
                    "basetype" : "OctetString",
                    "parent module" : {
                        "name" : "RFC1213-MIB",
                        "type" : "DisplayString",
                    },
                    "ranges" : [
                    {
                        "min" : "0",
                        "max" : "17"
                    },
                    ],
                    "range" : {
                        "min" : "0",
                        "max" : "17"
                    },
                },
            },
            "access" : "readonly",
            "description" :
                """Device name""",
        }, # scalar
        "serialNo" : {
            "nodetype" : "scalar",
            "moduleName" : "COMETMS-MIB",
            "oid" : "1.3.6.1.4.1.22626.1.4.1.3",
            "status" : "current",
            "syntax" : {
                "type" :                 {
                    "basetype" : "OctetString",
                    "parent module" : {
                        "name" : "RFC1213-MIB",
                        "type" : "DisplayString",
                    },
                    "ranges" : [
                    {
                        "min" : "0",
                        "max" : "8"
                    },
                    ],
                    "range" : {
                        "min" : "0",
                        "max" : "8"
                    },
                },
            },
            "access" : "readonly",
            "description" :
                """Device serial number""",
        }, # scalar
        "msType" : {
            "nodetype" : "scalar",
            "moduleName" : "COMETMS-MIB",
            "oid" : "1.3.6.1.4.1.22626.1.4.1.4",
            "status" : "current",
            "syntax" : {
                "type" :                 {
                    "basetype" : "Integer32",
                    "ranges" : [
                    {
                        "min" : "0",
                        "max" : "255"
                    },
                    ],
                    "range" : {
                        "min" : "0",
                        "max" : "255"
                    },
                },
            },
            "access" : "readonly",
            "description" :
                """MS type""",
        }, # scalar
        "selfTest" : {
            "nodetype" : "scalar",
            "moduleName" : "COMETMS-MIB",
            "oid" : "1.3.6.1.4.1.22626.1.4.1.5",
            "status" : "current",
            "syntax" : {
                "type" :                 {
                    "basetype" : "OctetString",
                    "parent module" : {
                        "name" : "RFC1213-MIB",
                        "type" : "DisplayString",
                    },
                    "ranges" : [
                    {
                        "min" : "0",
                        "max" : "30"
                    },
                    ],
                    "range" : {
                        "min" : "0",
                        "max" : "30"
                    },
                },
            },
            "access" : "readonly",
            "description" :
                """System selftest status""",
        }, # scalar
        "intAcc" : {
            "nodetype" : "scalar",
            "moduleName" : "COMETMS-MIB",
            "oid" : "1.3.6.1.4.1.22626.1.4.1.6",
            "status" : "current",
            "syntax" : {
                "type" :                 {
                    "basetype" : "Integer32",
                    "ranges" : [
                    {
                        "min" : "0",
                        "max" : "255"
                    },
                    ],
                    "range" : {
                        "min" : "0",
                        "max" : "255"
                    },
                },
            },
            "access" : "readonly",
            "description" :
                """Internal acoustic alarm""",
        }, # scalar
        "extAcc" : {
            "nodetype" : "scalar",
            "moduleName" : "COMETMS-MIB",
            "oid" : "1.3.6.1.4.1.22626.1.4.1.7",
            "status" : "current",
            "syntax" : {
                "type" :                 {
                    "basetype" : "Integer32",
                    "ranges" : [
                    {
                        "min" : "0",
                        "max" : "255"
                    },
                    ],
                    "range" : {
                        "min" : "0",
                        "max" : "255"
                    },
                },
            },
            "access" : "readonly",
            "description" :
                """Alarm out acoustic signalization""",
        }, # scalar
        "memUsg" : {
            "nodetype" : "scalar",
            "moduleName" : "COMETMS-MIB",
            "oid" : "1.3.6.1.4.1.22626.1.4.1.8",
            "status" : "current",
            "syntax" : {
                "type" :                 {
                    "basetype" : "Integer32",
                    "ranges" : [
                    {
                        "min" : "0",
                        "max" : "255"
                    },
                    ],
                    "range" : {
                        "min" : "0",
                        "max" : "255"
                    },
                },
            },
            "access" : "readonly",
            "description" :
                """Memory usage""",
        }, # scalar
        "channels" : {
            "nodetype" : "node",
            "moduleName" : "COMETMS-MIB",
            "oid" : "1.3.6.1.4.1.22626.1.4.2",
        }, # node
        "chTable" : {
            "nodetype" : "table",
            "moduleName" : "COMETMS-MIB",
            "oid" : "1.3.6.1.4.1.22626.1.4.2.1",
            "status" : "current",
            "description" :
                """Channels information table""",
        }, # table
        "chEntry" : {
            "nodetype" : "row",
            "moduleName" : "COMETMS-MIB",
            "oid" : "1.3.6.1.4.1.22626.1.4.2.1.1",
            "status" : "current",
            "linkage" : [
                "channelName",
            ],
            "description" :
                """Channels values entries""",
        }, # row
        "channelName" : {
            "nodetype" : "column",
            "moduleName" : "COMETMS-MIB",
            "oid" : "1.3.6.1.4.1.22626.1.4.2.1.1.1",
            "status" : "current",
            "syntax" : {
                "type" :                 {
                    "basetype" : "OctetString",
                    "parent module" : {
                        "name" : "RFC1213-MIB",
                        "type" : "DisplayString",
                    },
                    "ranges" : [
                    {
                        "min" : "0",
                        "max" : "17"
                    },
                    ],
                    "range" : {
                        "min" : "0",
                        "max" : "17"
                    },
                },
            },
            "access" : "readonly",
            "description" :
                """Channel name""",
        }, # column
        "channelValue" : {
            "nodetype" : "column",
            "moduleName" : "COMETMS-MIB",
            "oid" : "1.3.6.1.4.1.22626.1.4.2.1.1.2",
            "status" : "current",
            "syntax" : {
                "type" :                 {
                    "basetype" : "OctetString",
                    "parent module" : {
                        "name" : "RFC1213-MIB",
                        "type" : "DisplayString",
                    },
                    "ranges" : [
                    {
                        "min" : "0",
                        "max" : "40"
                    },
                    ],
                    "range" : {
                        "min" : "0",
                        "max" : "40"
                    },
                },
            },
            "access" : "readonly",
            "description" :
                """Channel value""",
        }, # column
        "channelInt" : {
            "nodetype" : "column",
            "moduleName" : "COMETMS-MIB",
            "oid" : "1.3.6.1.4.1.22626.1.4.2.1.1.3",
            "status" : "current",
            "syntax" : {
                "type" : { "module" :"", "name" : "Integer32"},
            },
            "access" : "readonly",
            "description" :
                """Channel int value (only real part, -2147483648 = error)""",
        }, # column
        "channelUnit" : {
            "nodetype" : "column",
            "moduleName" : "COMETMS-MIB",
            "oid" : "1.3.6.1.4.1.22626.1.4.2.1.1.4",
            "status" : "current",
            "syntax" : {
                "type" :                 {
                    "basetype" : "OctetString",
                    "parent module" : {
                        "name" : "RFC1213-MIB",
                        "type" : "DisplayString",
                    },
                    "ranges" : [
                    {
                        "min" : "0",
                        "max" : "17"
                    },
                    ],
                    "range" : {
                        "min" : "0",
                        "max" : "17"
                    },
                },
            },
            "access" : "readonly",
            "description" :
                """Channel unit""",
        }, # column
        "channelAlarm1" : {
            "nodetype" : "column",
            "moduleName" : "COMETMS-MIB",
            "oid" : "1.3.6.1.4.1.22626.1.4.2.1.1.5",
            "status" : "current",
            "syntax" : {
                "type" :                 {
                    "basetype" : "Integer32",
                    "ranges" : [
                    {
                        "min" : "0",
                        "max" : "255"
                    },
                    ],
                    "range" : {
                        "min" : "0",
                        "max" : "255"
                    },
                },
            },
            "access" : "readonly",
            "description" :
                """Alarm 1 state""",
        }, # column
        "channelAlarm2" : {
            "nodetype" : "column",
            "moduleName" : "COMETMS-MIB",
            "oid" : "1.3.6.1.4.1.22626.1.4.2.1.1.6",
            "status" : "current",
            "syntax" : {
                "type" :                 {
                    "basetype" : "Integer32",
                    "ranges" : [
                    {
                        "min" : "0",
                        "max" : "255"
                    },
                    ],
                    "range" : {
                        "min" : "0",
                        "max" : "255"
                    },
                },
            },
            "access" : "readonly",
            "description" :
                """Alarm 2 state""",
        }, # column
        "channelProces" : {
            "nodetype" : "column",
            "moduleName" : "COMETMS-MIB",
            "oid" : "1.3.6.1.4.1.22626.1.4.2.1.1.7",
            "status" : "current",
            "syntax" : {
                "type" :                 {
                    "basetype" : "OctetString",
                    "parent module" : {
                        "name" : "RFC1213-MIB",
                        "type" : "DisplayString",
                    },
                    "ranges" : [
                    {
                        "min" : "0",
                        "max" : "17"
                    },
                    ],
                    "range" : {
                        "min" : "0",
                        "max" : "17"
                    },
                },
            },
            "access" : "readonly",
            "description" :
                """Proces name""",
        }, # column
        "channelInt10" : {
            "nodetype" : "column",
            "moduleName" : "COMETMS-MIB",
            "oid" : "1.3.6.1.4.1.22626.1.4.2.1.1.8",
            "status" : "current",
            "syntax" : {
                "type" : { "module" :"", "name" : "Integer32"},
            },
            "access" : "readonly",
            "description" :
                """Channel int*10 value (22 = 2.2, -2147483648 = error)""",
        }, # column
        "channelInt100" : {
            "nodetype" : "column",
            "moduleName" : "COMETMS-MIB",
            "oid" : "1.3.6.1.4.1.22626.1.4.2.1.1.9",
            "status" : "current",
            "syntax" : {
                "type" : { "module" :"", "name" : "Integer32"},
            },
            "access" : "readonly",
            "description" :
                """Channel int*100 value (225 = 2.25, -2147483648 = error)""",
        }, # column
        "relay" : {
            "nodetype" : "node",
            "moduleName" : "COMETMS-MIB",
            "oid" : "1.3.6.1.4.1.22626.1.4.3",
        }, # node
        "rTable" : {
            "nodetype" : "table",
            "moduleName" : "COMETMS-MIB",
            "oid" : "1.3.6.1.4.1.22626.1.4.3.1",
            "status" : "current",
            "description" :
                """Relay board information table""",
        }, # table
        "rEntry" : {
            "nodetype" : "row",
            "moduleName" : "COMETMS-MIB",
            "oid" : "1.3.6.1.4.1.22626.1.4.3.1.1",
            "status" : "current",
            "linkage" : [
                "relayStateInt",
            ],
            "description" :
                """Relay board states entries""",
        }, # row
        "relayStateInt" : {
            "nodetype" : "column",
            "moduleName" : "COMETMS-MIB",
            "oid" : "1.3.6.1.4.1.22626.1.4.3.1.1.1",
            "status" : "current",
            "syntax" : {
                "type" :                 {
                    "basetype" : "Integer32",
                    "ranges" : [
                    {
                        "min" : "0",
                        "max" : "255"
                    },
                    ],
                    "range" : {
                        "min" : "0",
                        "max" : "255"
                    },
                },
            },
            "access" : "readonly",
            "description" :
                """Relay state Integer (0 = open, 1 = closed)""",
        }, # column
        "relayStateStr" : {
            "nodetype" : "column",
            "moduleName" : "COMETMS-MIB",
            "oid" : "1.3.6.1.4.1.22626.1.4.3.1.1.2",
            "status" : "current",
            "syntax" : {
                "type" :                 {
                    "basetype" : "OctetString",
                    "parent module" : {
                        "name" : "RFC1213-MIB",
                        "type" : "DisplayString",
                    },
                    "ranges" : [
                    {
                        "min" : "0",
                        "max" : "17"
                    },
                    ],
                    "range" : {
                        "min" : "0",
                        "max" : "17"
                    },
                },
            },
            "access" : "readonly",
            "description" :
                """Relay state String (open/closed)""",
        }, # column
    }, # nodes

}
