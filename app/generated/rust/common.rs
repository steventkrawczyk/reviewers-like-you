// This file is generated by rust-protobuf 3.1.0. Do not edit
// .proto file is parsed by protoc --rust-out=...
// @generated

// https://github.com/rust-lang/rust-clippy/issues/702
#![allow(unknown_lints)]
#![allow(clippy::all)]

#![allow(unused_attributes)]
#![cfg_attr(rustfmt, rustfmt::skip)]

#![allow(box_pointers)]
#![allow(dead_code)]
#![allow(missing_docs)]
#![allow(non_camel_case_types)]
#![allow(non_snake_case)]
#![allow(non_upper_case_globals)]
#![allow(trivial_casts)]
#![allow(unused_results)]
#![allow(unused_mut)]

//! Generated file from `common.proto`

/// Generated files are compatible only with the same version
/// of protobuf runtime.
const _PROTOBUF_VERSION_CHECK: () = ::protobuf::VERSION_3_1_0;

#[derive(PartialEq,Clone,Default,Debug)]
// @@protoc_insertion_point(message:proto.HealthCheckRequest)
pub struct HealthCheckRequest {
    // special fields
    // @@protoc_insertion_point(special_field:proto.HealthCheckRequest.special_fields)
    pub special_fields: ::protobuf::SpecialFields,
}

impl<'a> ::std::default::Default for &'a HealthCheckRequest {
    fn default() -> &'a HealthCheckRequest {
        <HealthCheckRequest as ::protobuf::Message>::default_instance()
    }
}

impl HealthCheckRequest {
    pub fn new() -> HealthCheckRequest {
        ::std::default::Default::default()
    }

    fn generated_message_descriptor_data() -> ::protobuf::reflect::GeneratedMessageDescriptorData {
        let mut fields = ::std::vec::Vec::with_capacity(0);
        let mut oneofs = ::std::vec::Vec::with_capacity(0);
        ::protobuf::reflect::GeneratedMessageDescriptorData::new_2::<HealthCheckRequest>(
            "HealthCheckRequest",
            fields,
            oneofs,
        )
    }
}

impl ::protobuf::Message for HealthCheckRequest {
    const NAME: &'static str = "HealthCheckRequest";

    fn is_initialized(&self) -> bool {
        true
    }

    fn merge_from(&mut self, is: &mut ::protobuf::CodedInputStream<'_>) -> ::protobuf::Result<()> {
        while let Some(tag) = is.read_raw_tag_or_eof()? {
            match tag {
                tag => {
                    ::protobuf::rt::read_unknown_or_skip_group(tag, is, self.special_fields.mut_unknown_fields())?;
                },
            };
        }
        ::std::result::Result::Ok(())
    }

    // Compute sizes of nested messages
    #[allow(unused_variables)]
    fn compute_size(&self) -> u64 {
        let mut my_size = 0;
        my_size += ::protobuf::rt::unknown_fields_size(self.special_fields.unknown_fields());
        self.special_fields.cached_size().set(my_size as u32);
        my_size
    }

    fn write_to_with_cached_sizes(&self, os: &mut ::protobuf::CodedOutputStream<'_>) -> ::protobuf::Result<()> {
        os.write_unknown_fields(self.special_fields.unknown_fields())?;
        ::std::result::Result::Ok(())
    }

    fn special_fields(&self) -> &::protobuf::SpecialFields {
        &self.special_fields
    }

    fn mut_special_fields(&mut self) -> &mut ::protobuf::SpecialFields {
        &mut self.special_fields
    }

    fn new() -> HealthCheckRequest {
        HealthCheckRequest::new()
    }

    fn clear(&mut self) {
        self.special_fields.clear();
    }

    fn default_instance() -> &'static HealthCheckRequest {
        static instance: HealthCheckRequest = HealthCheckRequest {
            special_fields: ::protobuf::SpecialFields::new(),
        };
        &instance
    }
}

impl ::protobuf::MessageFull for HealthCheckRequest {
    fn descriptor() -> ::protobuf::reflect::MessageDescriptor {
        static descriptor: ::protobuf::rt::Lazy<::protobuf::reflect::MessageDescriptor> = ::protobuf::rt::Lazy::new();
        descriptor.get(|| file_descriptor().message_by_package_relative_name("HealthCheckRequest").unwrap()).clone()
    }
}

impl ::std::fmt::Display for HealthCheckRequest {
    fn fmt(&self, f: &mut ::std::fmt::Formatter<'_>) -> ::std::fmt::Result {
        ::protobuf::text_format::fmt(self, f)
    }
}

impl ::protobuf::reflect::ProtobufValue for HealthCheckRequest {
    type RuntimeType = ::protobuf::reflect::rt::RuntimeTypeMessage<Self>;
}

#[derive(PartialEq,Clone,Default,Debug)]
// @@protoc_insertion_point(message:proto.Payload)
pub struct Payload {
    // message fields
    // @@protoc_insertion_point(field:proto.Payload.message)
    pub message: ::std::option::Option<::std::string::String>,
    // @@protoc_insertion_point(field:proto.Payload.category)
    pub category: ::std::option::Option<::std::string::String>,
    // @@protoc_insertion_point(field:proto.Payload.status)
    pub status: ::std::option::Option<i32>,
    // @@protoc_insertion_point(field:proto.Payload.data)
    pub data: ::std::option::Option<::std::string::String>,
    // special fields
    // @@protoc_insertion_point(special_field:proto.Payload.special_fields)
    pub special_fields: ::protobuf::SpecialFields,
}

impl<'a> ::std::default::Default for &'a Payload {
    fn default() -> &'a Payload {
        <Payload as ::protobuf::Message>::default_instance()
    }
}

impl Payload {
    pub fn new() -> Payload {
        ::std::default::Default::default()
    }

    fn generated_message_descriptor_data() -> ::protobuf::reflect::GeneratedMessageDescriptorData {
        let mut fields = ::std::vec::Vec::with_capacity(4);
        let mut oneofs = ::std::vec::Vec::with_capacity(0);
        fields.push(::protobuf::reflect::rt::v2::make_option_accessor::<_, _>(
            "message",
            |m: &Payload| { &m.message },
            |m: &mut Payload| { &mut m.message },
        ));
        fields.push(::protobuf::reflect::rt::v2::make_option_accessor::<_, _>(
            "category",
            |m: &Payload| { &m.category },
            |m: &mut Payload| { &mut m.category },
        ));
        fields.push(::protobuf::reflect::rt::v2::make_option_accessor::<_, _>(
            "status",
            |m: &Payload| { &m.status },
            |m: &mut Payload| { &mut m.status },
        ));
        fields.push(::protobuf::reflect::rt::v2::make_option_accessor::<_, _>(
            "data",
            |m: &Payload| { &m.data },
            |m: &mut Payload| { &mut m.data },
        ));
        ::protobuf::reflect::GeneratedMessageDescriptorData::new_2::<Payload>(
            "Payload",
            fields,
            oneofs,
        )
    }
}

impl ::protobuf::Message for Payload {
    const NAME: &'static str = "Payload";

    fn is_initialized(&self) -> bool {
        true
    }

    fn merge_from(&mut self, is: &mut ::protobuf::CodedInputStream<'_>) -> ::protobuf::Result<()> {
        while let Some(tag) = is.read_raw_tag_or_eof()? {
            match tag {
                10 => {
                    self.message = ::std::option::Option::Some(is.read_string()?);
                },
                18 => {
                    self.category = ::std::option::Option::Some(is.read_string()?);
                },
                24 => {
                    self.status = ::std::option::Option::Some(is.read_int32()?);
                },
                34 => {
                    self.data = ::std::option::Option::Some(is.read_string()?);
                },
                tag => {
                    ::protobuf::rt::read_unknown_or_skip_group(tag, is, self.special_fields.mut_unknown_fields())?;
                },
            };
        }
        ::std::result::Result::Ok(())
    }

    // Compute sizes of nested messages
    #[allow(unused_variables)]
    fn compute_size(&self) -> u64 {
        let mut my_size = 0;
        if let Some(v) = self.message.as_ref() {
            my_size += ::protobuf::rt::string_size(1, &v);
        }
        if let Some(v) = self.category.as_ref() {
            my_size += ::protobuf::rt::string_size(2, &v);
        }
        if let Some(v) = self.status {
            my_size += ::protobuf::rt::int32_size(3, v);
        }
        if let Some(v) = self.data.as_ref() {
            my_size += ::protobuf::rt::string_size(4, &v);
        }
        my_size += ::protobuf::rt::unknown_fields_size(self.special_fields.unknown_fields());
        self.special_fields.cached_size().set(my_size as u32);
        my_size
    }

    fn write_to_with_cached_sizes(&self, os: &mut ::protobuf::CodedOutputStream<'_>) -> ::protobuf::Result<()> {
        if let Some(v) = self.message.as_ref() {
            os.write_string(1, v)?;
        }
        if let Some(v) = self.category.as_ref() {
            os.write_string(2, v)?;
        }
        if let Some(v) = self.status {
            os.write_int32(3, v)?;
        }
        if let Some(v) = self.data.as_ref() {
            os.write_string(4, v)?;
        }
        os.write_unknown_fields(self.special_fields.unknown_fields())?;
        ::std::result::Result::Ok(())
    }

    fn special_fields(&self) -> &::protobuf::SpecialFields {
        &self.special_fields
    }

    fn mut_special_fields(&mut self) -> &mut ::protobuf::SpecialFields {
        &mut self.special_fields
    }

    fn new() -> Payload {
        Payload::new()
    }

    fn clear(&mut self) {
        self.message = ::std::option::Option::None;
        self.category = ::std::option::Option::None;
        self.status = ::std::option::Option::None;
        self.data = ::std::option::Option::None;
        self.special_fields.clear();
    }

    fn default_instance() -> &'static Payload {
        static instance: Payload = Payload {
            message: ::std::option::Option::None,
            category: ::std::option::Option::None,
            status: ::std::option::Option::None,
            data: ::std::option::Option::None,
            special_fields: ::protobuf::SpecialFields::new(),
        };
        &instance
    }
}

impl ::protobuf::MessageFull for Payload {
    fn descriptor() -> ::protobuf::reflect::MessageDescriptor {
        static descriptor: ::protobuf::rt::Lazy<::protobuf::reflect::MessageDescriptor> = ::protobuf::rt::Lazy::new();
        descriptor.get(|| file_descriptor().message_by_package_relative_name("Payload").unwrap()).clone()
    }
}

impl ::std::fmt::Display for Payload {
    fn fmt(&self, f: &mut ::std::fmt::Formatter<'_>) -> ::std::fmt::Result {
        ::protobuf::text_format::fmt(self, f)
    }
}

impl ::protobuf::reflect::ProtobufValue for Payload {
    type RuntimeType = ::protobuf::reflect::rt::RuntimeTypeMessage<Self>;
}

static file_descriptor_proto_data: &'static [u8] = b"\
    \n\x0ccommon.proto\x12\x05proto\"\x14\n\x12HealthCheckRequest\"\xac\x01\
    \n\x07Payload\x12\x1d\n\x07message\x18\x01\x20\x01(\tH\0R\x07message\x88\
    \x01\x01\x12\x1f\n\x08category\x18\x02\x20\x01(\tH\x01R\x08category\x88\
    \x01\x01\x12\x1b\n\x06status\x18\x03\x20\x01(\x05H\x02R\x06status\x88\
    \x01\x01\x12\x17\n\x04data\x18\x04\x20\x01(\tH\x03R\x04data\x88\x01\x01B\
    \n\n\x08_messageB\x0b\n\t_categoryB\t\n\x07_statusB\x07\n\x05_dataB\x18Z\
    \x16app/generated/go/protoJ\xf4\x02\n\x06\x12\x04\0\0\r\x01\n\x08\n\x01\
    \x0c\x12\x03\0\0\x12\n\x08\n\x01\x02\x12\x03\x02\0\x0e\n\x08\n\x01\x08\
    \x12\x03\x04\0-\n\t\n\x02\x08\x0b\x12\x03\x04\0-\n\t\n\x02\x04\0\x12\x03\
    \x06\0\x1d\n\n\n\x03\x04\0\x01\x12\x03\x06\x08\x1a\n\n\n\x02\x04\x01\x12\
    \x04\x08\0\r\x01\n\n\n\x03\x04\x01\x01\x12\x03\x08\x08\x0f\n\x0b\n\x04\
    \x04\x01\x02\0\x12\x03\t\x02\x1e\n\x0c\n\x05\x04\x01\x02\0\x04\x12\x03\t\
    \x02\n\n\x0c\n\x05\x04\x01\x02\0\x05\x12\x03\t\x0b\x11\n\x0c\n\x05\x04\
    \x01\x02\0\x01\x12\x03\t\x12\x19\n\x0c\n\x05\x04\x01\x02\0\x03\x12\x03\t\
    \x1c\x1d\n\x0b\n\x04\x04\x01\x02\x01\x12\x03\n\x02\x1f\n\x0c\n\x05\x04\
    \x01\x02\x01\x04\x12\x03\n\x02\n\n\x0c\n\x05\x04\x01\x02\x01\x05\x12\x03\
    \n\x0b\x11\n\x0c\n\x05\x04\x01\x02\x01\x01\x12\x03\n\x12\x1a\n\x0c\n\x05\
    \x04\x01\x02\x01\x03\x12\x03\n\x1d\x1e\n\x0b\n\x04\x04\x01\x02\x02\x12\
    \x03\x0b\x02\x1c\n\x0c\n\x05\x04\x01\x02\x02\x04\x12\x03\x0b\x02\n\n\x0c\
    \n\x05\x04\x01\x02\x02\x05\x12\x03\x0b\x0b\x10\n\x0c\n\x05\x04\x01\x02\
    \x02\x01\x12\x03\x0b\x11\x17\n\x0c\n\x05\x04\x01\x02\x02\x03\x12\x03\x0b\
    \x1a\x1b\n\x0b\n\x04\x04\x01\x02\x03\x12\x03\x0c\x02\x1b\n\x0c\n\x05\x04\
    \x01\x02\x03\x04\x12\x03\x0c\x02\n\n\x0c\n\x05\x04\x01\x02\x03\x05\x12\
    \x03\x0c\x0b\x11\n\x0c\n\x05\x04\x01\x02\x03\x01\x12\x03\x0c\x12\x16\n\
    \x0c\n\x05\x04\x01\x02\x03\x03\x12\x03\x0c\x19\x1ab\x06proto3\
";

/// `FileDescriptorProto` object which was a source for this generated file
fn file_descriptor_proto() -> &'static ::protobuf::descriptor::FileDescriptorProto {
    static file_descriptor_proto_lazy: ::protobuf::rt::Lazy<::protobuf::descriptor::FileDescriptorProto> = ::protobuf::rt::Lazy::new();
    file_descriptor_proto_lazy.get(|| {
        ::protobuf::Message::parse_from_bytes(file_descriptor_proto_data).unwrap()
    })
}

/// `FileDescriptor` object which allows dynamic access to files
pub fn file_descriptor() -> &'static ::protobuf::reflect::FileDescriptor {
    static generated_file_descriptor_lazy: ::protobuf::rt::Lazy<::protobuf::reflect::GeneratedFileDescriptor> = ::protobuf::rt::Lazy::new();
    static file_descriptor: ::protobuf::rt::Lazy<::protobuf::reflect::FileDescriptor> = ::protobuf::rt::Lazy::new();
    file_descriptor.get(|| {
        let generated_file_descriptor = generated_file_descriptor_lazy.get(|| {
            let mut deps = ::std::vec::Vec::with_capacity(0);
            let mut messages = ::std::vec::Vec::with_capacity(2);
            messages.push(HealthCheckRequest::generated_message_descriptor_data());
            messages.push(Payload::generated_message_descriptor_data());
            let mut enums = ::std::vec::Vec::with_capacity(0);
            ::protobuf::reflect::GeneratedFileDescriptor::new_generated(
                file_descriptor_proto(),
                deps,
                messages,
                enums,
            )
        });
        ::protobuf::reflect::FileDescriptor::new_generated_2(generated_file_descriptor)
    })
}