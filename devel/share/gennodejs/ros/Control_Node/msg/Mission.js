// Auto-generated. Do not edit!

// (in-package Control_Node.msg)


"use strict";

const _serializer = _ros_msg_utils.Serialize;
const _arraySerializer = _serializer.Array;
const _deserializer = _ros_msg_utils.Deserialize;
const _arrayDeserializer = _deserializer.Array;
const _finder = _ros_msg_utils.Find;
const _getByteLength = _ros_msg_utils.getByteLength;

//-----------------------------------------------------------

class Mission {
  constructor(initObj={}) {
    if (initObj === null) {
      // initObj === null is a special case for deserialization where we don't initialize fields
      this.traffic = null;
      this.parking = null;
      this.crossbar = null;
      this.tunnel = null;
    }
    else {
      if (initObj.hasOwnProperty('traffic')) {
        this.traffic = initObj.traffic
      }
      else {
        this.traffic = false;
      }
      if (initObj.hasOwnProperty('parking')) {
        this.parking = initObj.parking
      }
      else {
        this.parking = false;
      }
      if (initObj.hasOwnProperty('crossbar')) {
        this.crossbar = initObj.crossbar
      }
      else {
        this.crossbar = false;
      }
      if (initObj.hasOwnProperty('tunnel')) {
        this.tunnel = initObj.tunnel
      }
      else {
        this.tunnel = false;
      }
    }
  }

  static serialize(obj, buffer, bufferOffset) {
    // Serializes a message object of type Mission
    // Serialize message field [traffic]
    bufferOffset = _serializer.bool(obj.traffic, buffer, bufferOffset);
    // Serialize message field [parking]
    bufferOffset = _serializer.bool(obj.parking, buffer, bufferOffset);
    // Serialize message field [crossbar]
    bufferOffset = _serializer.bool(obj.crossbar, buffer, bufferOffset);
    // Serialize message field [tunnel]
    bufferOffset = _serializer.bool(obj.tunnel, buffer, bufferOffset);
    return bufferOffset;
  }

  static deserialize(buffer, bufferOffset=[0]) {
    //deserializes a message object of type Mission
    let len;
    let data = new Mission(null);
    // Deserialize message field [traffic]
    data.traffic = _deserializer.bool(buffer, bufferOffset);
    // Deserialize message field [parking]
    data.parking = _deserializer.bool(buffer, bufferOffset);
    // Deserialize message field [crossbar]
    data.crossbar = _deserializer.bool(buffer, bufferOffset);
    // Deserialize message field [tunnel]
    data.tunnel = _deserializer.bool(buffer, bufferOffset);
    return data;
  }

  static getMessageSize(object) {
    return 4;
  }

  static datatype() {
    // Returns string type for a message object
    return 'Control_Node/Mission';
  }

  static md5sum() {
    //Returns md5sum for a message object
    return '132b675c11a085c243deb3519223ef08';
  }

  static messageDefinition() {
    // Returns full string definition for message
    return `
    bool traffic
    bool parking
    bool crossbar
    bool tunnel
    `;
  }

  static Resolve(msg) {
    // deep-construct a valid message object instance of whatever was passed in
    if (typeof msg !== 'object' || msg === null) {
      msg = {};
    }
    const resolved = new Mission(null);
    if (msg.traffic !== undefined) {
      resolved.traffic = msg.traffic;
    }
    else {
      resolved.traffic = false
    }

    if (msg.parking !== undefined) {
      resolved.parking = msg.parking;
    }
    else {
      resolved.parking = false
    }

    if (msg.crossbar !== undefined) {
      resolved.crossbar = msg.crossbar;
    }
    else {
      resolved.crossbar = false
    }

    if (msg.tunnel !== undefined) {
      resolved.tunnel = msg.tunnel;
    }
    else {
      resolved.tunnel = false
    }

    return resolved;
    }
};

module.exports = Mission;
