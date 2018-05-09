// Auto-generated. Do not edit!

// (in-package ImageProcess_Node.srv)


"use strict";

const _serializer = _ros_msg_utils.Serialize;
const _arraySerializer = _serializer.Array;
const _deserializer = _ros_msg_utils.Deserialize;
const _arrayDeserializer = _deserializer.Array;
const _finder = _ros_msg_utils.Find;
const _getByteLength = _ros_msg_utils.getByteLength;

//-----------------------------------------------------------


//-----------------------------------------------------------

class DetectRequest {
  constructor(initObj={}) {
    if (initObj === null) {
      // initObj === null is a special case for deserialization where we don't initialize fields
      this.roi_image = null;
    }
    else {
      if (initObj.hasOwnProperty('roi_image')) {
        this.roi_image = initObj.roi_image
      }
      else {
        this.roi_image = 0.0;
      }
    }
  }

  static serialize(obj, buffer, bufferOffset) {
    // Serializes a message object of type DetectRequest
    // Serialize message field [roi_image]
    bufferOffset = _serializer.float32(obj.roi_image, buffer, bufferOffset);
    return bufferOffset;
  }

  static deserialize(buffer, bufferOffset=[0]) {
    //deserializes a message object of type DetectRequest
    let len;
    let data = new DetectRequest(null);
    // Deserialize message field [roi_image]
    data.roi_image = _deserializer.float32(buffer, bufferOffset);
    return data;
  }

  static getMessageSize(object) {
    return 4;
  }

  static datatype() {
    // Returns string type for a service object
    return 'ImageProcess_Node/DetectRequest';
  }

  static md5sum() {
    //Returns md5sum for a message object
    return '0e029041da4e771f12f774b5957b1650';
  }

  static messageDefinition() {
    // Returns full string definition for message
    return `
    float32 roi_image
    
    `;
  }

  static Resolve(msg) {
    // deep-construct a valid message object instance of whatever was passed in
    if (typeof msg !== 'object' || msg === null) {
      msg = {};
    }
    const resolved = new DetectRequest(null);
    if (msg.roi_image !== undefined) {
      resolved.roi_image = msg.roi_image;
    }
    else {
      resolved.roi_image = 0.0
    }

    return resolved;
    }
};

class DetectResponse {
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
        this.result = '';
      }
    }
  }

  static serialize(obj, buffer, bufferOffset) {
    // Serializes a message object of type DetectResponse
    // Serialize message field [result]
    bufferOffset = _serializer.string(obj.result, buffer, bufferOffset);
    return bufferOffset;
  }

  static deserialize(buffer, bufferOffset=[0]) {
    //deserializes a message object of type DetectResponse
    let len;
    let data = new DetectResponse(null);
    // Deserialize message field [result]
    data.result = _deserializer.string(buffer, bufferOffset);
    return data;
  }

  static getMessageSize(object) {
    let length = 0;
    length += object.result.length;
    return length + 4;
  }

  static datatype() {
    // Returns string type for a service object
    return 'ImageProcess_Node/DetectResponse';
  }

  static md5sum() {
    //Returns md5sum for a message object
    return 'c22f2a1ed8654a0b365f1bb3f7ff2c0f';
  }

  static messageDefinition() {
    // Returns full string definition for message
    return `
    string result
    
    `;
  }

  static Resolve(msg) {
    // deep-construct a valid message object instance of whatever was passed in
    if (typeof msg !== 'object' || msg === null) {
      msg = {};
    }
    const resolved = new DetectResponse(null);
    if (msg.result !== undefined) {
      resolved.result = msg.result;
    }
    else {
      resolved.result = ''
    }

    return resolved;
    }
};

module.exports = {
  Request: DetectRequest,
  Response: DetectResponse,
  md5sum() { return 'c5cdbbf937a2b7afdb40f16147414b23'; },
  datatype() { return 'ImageProcess_Node/Detect'; }
};
