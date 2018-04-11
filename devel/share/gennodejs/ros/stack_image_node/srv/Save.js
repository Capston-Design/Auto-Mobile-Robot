// Auto-generated. Do not edit!

// (in-package stack_image_node.srv)


"use strict";

const _serializer = _ros_msg_utils.Serialize;
const _arraySerializer = _serializer.Array;
const _deserializer = _ros_msg_utils.Deserialize;
const _arrayDeserializer = _deserializer.Array;
const _finder = _ros_msg_utils.Find;
const _getByteLength = _ros_msg_utils.getByteLength;

//-----------------------------------------------------------


//-----------------------------------------------------------

class SaveRequest {
  constructor(initObj={}) {
    if (initObj === null) {
      // initObj === null is a special case for deserialization where we don't initialize fields
      this.flag_message = null;
    }
    else {
      if (initObj.hasOwnProperty('flag_message')) {
        this.flag_message = initObj.flag_message
      }
      else {
        this.flag_message = '';
      }
    }
  }

  static serialize(obj, buffer, bufferOffset) {
    // Serializes a message object of type SaveRequest
    // Serialize message field [flag_message]
    bufferOffset = _serializer.string(obj.flag_message, buffer, bufferOffset);
    return bufferOffset;
  }

  static deserialize(buffer, bufferOffset=[0]) {
    //deserializes a message object of type SaveRequest
    let len;
    let data = new SaveRequest(null);
    // Deserialize message field [flag_message]
    data.flag_message = _deserializer.string(buffer, bufferOffset);
    return data;
  }

  static getMessageSize(object) {
    let length = 0;
    length += object.flag_message.length;
    return length + 4;
  }

  static datatype() {
    // Returns string type for a service object
    return 'stack_image_node/SaveRequest';
  }

  static md5sum() {
    //Returns md5sum for a message object
    return '14fdb931223464f74c4be57e81a7ef44';
  }

  static messageDefinition() {
    // Returns full string definition for message
    return `
    string flag_message
    
    `;
  }

  static Resolve(msg) {
    // deep-construct a valid message object instance of whatever was passed in
    if (typeof msg !== 'object' || msg === null) {
      msg = {};
    }
    const resolved = new SaveRequest(null);
    if (msg.flag_message !== undefined) {
      resolved.flag_message = msg.flag_message;
    }
    else {
      resolved.flag_message = ''
    }

    return resolved;
    }
};

class SaveResponse {
  constructor(initObj={}) {
    if (initObj === null) {
      // initObj === null is a special case for deserialization where we don't initialize fields
      this.result = null;
    }
    else {
      if (initObj.hasOwnProperty('result')) {
        this.result = initObj.result
      }
      else {
        this.result = false;
      }
    }
  }

  static serialize(obj, buffer, bufferOffset) {
    // Serializes a message object of type SaveResponse
    // Serialize message field [result]
    bufferOffset = _serializer.bool(obj.result, buffer, bufferOffset);
    return bufferOffset;
  }

  static deserialize(buffer, bufferOffset=[0]) {
    //deserializes a message object of type SaveResponse
    let len;
    let data = new SaveResponse(null);
    // Deserialize message field [result]
    data.result = _deserializer.bool(buffer, bufferOffset);
    return data;
  }

  static getMessageSize(object) {
    return 1;
  }

  static datatype() {
    // Returns string type for a service object
    return 'stack_image_node/SaveResponse';
  }

  static md5sum() {
    //Returns md5sum for a message object
    return 'eb13ac1f1354ccecb7941ee8fa2192e8';
  }

  static messageDefinition() {
    // Returns full string definition for message
    return `
    bool result
    
    `;
  }

  static Resolve(msg) {
    // deep-construct a valid message object instance of whatever was passed in
    if (typeof msg !== 'object' || msg === null) {
      msg = {};
    }
    const resolved = new SaveResponse(null);
    if (msg.result !== undefined) {
      resolved.result = msg.result;
    }
    else {
      resolved.result = false
    }

    return resolved;
    }
};

module.exports = {
  Request: SaveRequest,
  Response: SaveResponse,
  md5sum() { return '2c75fafdcb7a71b1c42c8cdb584b2cf6'; },
  datatype() { return 'stack_image_node/Save'; }
};
