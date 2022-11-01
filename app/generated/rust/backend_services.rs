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

//! Generated file from `backend_services.proto`

/// Generated files are compatible only with the same version
/// of protobuf runtime.
const _PROTOBUF_VERSION_CHECK: () = ::protobuf::VERSION_3_1_0;

#[derive(PartialEq,Clone,Default,Debug)]
// @@protoc_insertion_point(message:proto.Vector)
pub struct Vector {
    // message fields
    // @@protoc_insertion_point(field:proto.Vector.entry)
    pub entry: ::std::vec::Vec<f32>,
    // special fields
    // @@protoc_insertion_point(special_field:proto.Vector.special_fields)
    pub special_fields: ::protobuf::SpecialFields,
}

impl<'a> ::std::default::Default for &'a Vector {
    fn default() -> &'a Vector {
        <Vector as ::protobuf::Message>::default_instance()
    }
}

impl Vector {
    pub fn new() -> Vector {
        ::std::default::Default::default()
    }

    fn generated_message_descriptor_data() -> ::protobuf::reflect::GeneratedMessageDescriptorData {
        let mut fields = ::std::vec::Vec::with_capacity(1);
        let mut oneofs = ::std::vec::Vec::with_capacity(0);
        fields.push(::protobuf::reflect::rt::v2::make_vec_simpler_accessor::<_, _>(
            "entry",
            |m: &Vector| { &m.entry },
            |m: &mut Vector| { &mut m.entry },
        ));
        ::protobuf::reflect::GeneratedMessageDescriptorData::new_2::<Vector>(
            "Vector",
            fields,
            oneofs,
        )
    }
}

impl ::protobuf::Message for Vector {
    const NAME: &'static str = "Vector";

    fn is_initialized(&self) -> bool {
        true
    }

    fn merge_from(&mut self, is: &mut ::protobuf::CodedInputStream<'_>) -> ::protobuf::Result<()> {
        while let Some(tag) = is.read_raw_tag_or_eof()? {
            match tag {
                10 => {
                    is.read_repeated_packed_float_into(&mut self.entry)?;
                },
                13 => {
                    self.entry.push(is.read_float()?);
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
        my_size += 5 * self.entry.len() as u64;
        my_size += ::protobuf::rt::unknown_fields_size(self.special_fields.unknown_fields());
        self.special_fields.cached_size().set(my_size as u32);
        my_size
    }

    fn write_to_with_cached_sizes(&self, os: &mut ::protobuf::CodedOutputStream<'_>) -> ::protobuf::Result<()> {
        for v in &self.entry {
            os.write_float(1, *v)?;
        };
        os.write_unknown_fields(self.special_fields.unknown_fields())?;
        ::std::result::Result::Ok(())
    }

    fn special_fields(&self) -> &::protobuf::SpecialFields {
        &self.special_fields
    }

    fn mut_special_fields(&mut self) -> &mut ::protobuf::SpecialFields {
        &mut self.special_fields
    }

    fn new() -> Vector {
        Vector::new()
    }

    fn clear(&mut self) {
        self.entry.clear();
        self.special_fields.clear();
    }

    fn default_instance() -> &'static Vector {
        static instance: Vector = Vector {
            entry: ::std::vec::Vec::new(),
            special_fields: ::protobuf::SpecialFields::new(),
        };
        &instance
    }
}

impl ::protobuf::MessageFull for Vector {
    fn descriptor() -> ::protobuf::reflect::MessageDescriptor {
        static descriptor: ::protobuf::rt::Lazy<::protobuf::reflect::MessageDescriptor> = ::protobuf::rt::Lazy::new();
        descriptor.get(|| file_descriptor().message_by_package_relative_name("Vector").unwrap()).clone()
    }
}

impl ::std::fmt::Display for Vector {
    fn fmt(&self, f: &mut ::std::fmt::Formatter<'_>) -> ::std::fmt::Result {
        ::protobuf::text_format::fmt(self, f)
    }
}

impl ::protobuf::reflect::ProtobufValue for Vector {
    type RuntimeType = ::protobuf::reflect::rt::RuntimeTypeMessage<Self>;
}

#[derive(PartialEq,Clone,Default,Debug)]
// @@protoc_insertion_point(message:proto.GetClosestNeighborRequest)
pub struct GetClosestNeighborRequest {
    // message fields
    // @@protoc_insertion_point(field:proto.GetClosestNeighborRequest.vector)
    pub vector: ::protobuf::MessageField<Vector>,
    // special fields
    // @@protoc_insertion_point(special_field:proto.GetClosestNeighborRequest.special_fields)
    pub special_fields: ::protobuf::SpecialFields,
}

impl<'a> ::std::default::Default for &'a GetClosestNeighborRequest {
    fn default() -> &'a GetClosestNeighborRequest {
        <GetClosestNeighborRequest as ::protobuf::Message>::default_instance()
    }
}

impl GetClosestNeighborRequest {
    pub fn new() -> GetClosestNeighborRequest {
        ::std::default::Default::default()
    }

    fn generated_message_descriptor_data() -> ::protobuf::reflect::GeneratedMessageDescriptorData {
        let mut fields = ::std::vec::Vec::with_capacity(1);
        let mut oneofs = ::std::vec::Vec::with_capacity(0);
        fields.push(::protobuf::reflect::rt::v2::make_message_field_accessor::<_, Vector>(
            "vector",
            |m: &GetClosestNeighborRequest| { &m.vector },
            |m: &mut GetClosestNeighborRequest| { &mut m.vector },
        ));
        ::protobuf::reflect::GeneratedMessageDescriptorData::new_2::<GetClosestNeighborRequest>(
            "GetClosestNeighborRequest",
            fields,
            oneofs,
        )
    }
}

impl ::protobuf::Message for GetClosestNeighborRequest {
    const NAME: &'static str = "GetClosestNeighborRequest";

    fn is_initialized(&self) -> bool {
        true
    }

    fn merge_from(&mut self, is: &mut ::protobuf::CodedInputStream<'_>) -> ::protobuf::Result<()> {
        while let Some(tag) = is.read_raw_tag_or_eof()? {
            match tag {
                10 => {
                    ::protobuf::rt::read_singular_message_into_field(is, &mut self.vector)?;
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
        if let Some(v) = self.vector.as_ref() {
            let len = v.compute_size();
            my_size += 1 + ::protobuf::rt::compute_raw_varint64_size(len) + len;
        }
        my_size += ::protobuf::rt::unknown_fields_size(self.special_fields.unknown_fields());
        self.special_fields.cached_size().set(my_size as u32);
        my_size
    }

    fn write_to_with_cached_sizes(&self, os: &mut ::protobuf::CodedOutputStream<'_>) -> ::protobuf::Result<()> {
        if let Some(v) = self.vector.as_ref() {
            ::protobuf::rt::write_message_field_with_cached_size(1, v, os)?;
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

    fn new() -> GetClosestNeighborRequest {
        GetClosestNeighborRequest::new()
    }

    fn clear(&mut self) {
        self.vector.clear();
        self.special_fields.clear();
    }

    fn default_instance() -> &'static GetClosestNeighborRequest {
        static instance: GetClosestNeighborRequest = GetClosestNeighborRequest {
            vector: ::protobuf::MessageField::none(),
            special_fields: ::protobuf::SpecialFields::new(),
        };
        &instance
    }
}

impl ::protobuf::MessageFull for GetClosestNeighborRequest {
    fn descriptor() -> ::protobuf::reflect::MessageDescriptor {
        static descriptor: ::protobuf::rt::Lazy<::protobuf::reflect::MessageDescriptor> = ::protobuf::rt::Lazy::new();
        descriptor.get(|| file_descriptor().message_by_package_relative_name("GetClosestNeighborRequest").unwrap()).clone()
    }
}

impl ::std::fmt::Display for GetClosestNeighborRequest {
    fn fmt(&self, f: &mut ::std::fmt::Formatter<'_>) -> ::std::fmt::Result {
        ::protobuf::text_format::fmt(self, f)
    }
}

impl ::protobuf::reflect::ProtobufValue for GetClosestNeighborRequest {
    type RuntimeType = ::protobuf::reflect::rt::RuntimeTypeMessage<Self>;
}

#[derive(PartialEq,Clone,Default,Debug)]
// @@protoc_insertion_point(message:proto.GetClosestNeighborResponse)
pub struct GetClosestNeighborResponse {
    // message fields
    // @@protoc_insertion_point(field:proto.GetClosestNeighborResponse.author)
    pub author: ::std::option::Option<::std::string::String>,
    // special fields
    // @@protoc_insertion_point(special_field:proto.GetClosestNeighborResponse.special_fields)
    pub special_fields: ::protobuf::SpecialFields,
}

impl<'a> ::std::default::Default for &'a GetClosestNeighborResponse {
    fn default() -> &'a GetClosestNeighborResponse {
        <GetClosestNeighborResponse as ::protobuf::Message>::default_instance()
    }
}

impl GetClosestNeighborResponse {
    pub fn new() -> GetClosestNeighborResponse {
        ::std::default::Default::default()
    }

    fn generated_message_descriptor_data() -> ::protobuf::reflect::GeneratedMessageDescriptorData {
        let mut fields = ::std::vec::Vec::with_capacity(1);
        let mut oneofs = ::std::vec::Vec::with_capacity(0);
        fields.push(::protobuf::reflect::rt::v2::make_option_accessor::<_, _>(
            "author",
            |m: &GetClosestNeighborResponse| { &m.author },
            |m: &mut GetClosestNeighborResponse| { &mut m.author },
        ));
        ::protobuf::reflect::GeneratedMessageDescriptorData::new_2::<GetClosestNeighborResponse>(
            "GetClosestNeighborResponse",
            fields,
            oneofs,
        )
    }
}

impl ::protobuf::Message for GetClosestNeighborResponse {
    const NAME: &'static str = "GetClosestNeighborResponse";

    fn is_initialized(&self) -> bool {
        true
    }

    fn merge_from(&mut self, is: &mut ::protobuf::CodedInputStream<'_>) -> ::protobuf::Result<()> {
        while let Some(tag) = is.read_raw_tag_or_eof()? {
            match tag {
                10 => {
                    self.author = ::std::option::Option::Some(is.read_string()?);
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
        if let Some(v) = self.author.as_ref() {
            my_size += ::protobuf::rt::string_size(1, &v);
        }
        my_size += ::protobuf::rt::unknown_fields_size(self.special_fields.unknown_fields());
        self.special_fields.cached_size().set(my_size as u32);
        my_size
    }

    fn write_to_with_cached_sizes(&self, os: &mut ::protobuf::CodedOutputStream<'_>) -> ::protobuf::Result<()> {
        if let Some(v) = self.author.as_ref() {
            os.write_string(1, v)?;
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

    fn new() -> GetClosestNeighborResponse {
        GetClosestNeighborResponse::new()
    }

    fn clear(&mut self) {
        self.author = ::std::option::Option::None;
        self.special_fields.clear();
    }

    fn default_instance() -> &'static GetClosestNeighborResponse {
        static instance: GetClosestNeighborResponse = GetClosestNeighborResponse {
            author: ::std::option::Option::None,
            special_fields: ::protobuf::SpecialFields::new(),
        };
        &instance
    }
}

impl ::protobuf::MessageFull for GetClosestNeighborResponse {
    fn descriptor() -> ::protobuf::reflect::MessageDescriptor {
        static descriptor: ::protobuf::rt::Lazy<::protobuf::reflect::MessageDescriptor> = ::protobuf::rt::Lazy::new();
        descriptor.get(|| file_descriptor().message_by_package_relative_name("GetClosestNeighborResponse").unwrap()).clone()
    }
}

impl ::std::fmt::Display for GetClosestNeighborResponse {
    fn fmt(&self, f: &mut ::std::fmt::Formatter<'_>) -> ::std::fmt::Result {
        ::protobuf::text_format::fmt(self, f)
    }
}

impl ::protobuf::reflect::ProtobufValue for GetClosestNeighborResponse {
    type RuntimeType = ::protobuf::reflect::rt::RuntimeTypeMessage<Self>;
}

#[derive(PartialEq,Clone,Default,Debug)]
// @@protoc_insertion_point(message:proto.FindAverageVectorRequest)
pub struct FindAverageVectorRequest {
    // special fields
    // @@protoc_insertion_point(special_field:proto.FindAverageVectorRequest.special_fields)
    pub special_fields: ::protobuf::SpecialFields,
}

impl<'a> ::std::default::Default for &'a FindAverageVectorRequest {
    fn default() -> &'a FindAverageVectorRequest {
        <FindAverageVectorRequest as ::protobuf::Message>::default_instance()
    }
}

impl FindAverageVectorRequest {
    pub fn new() -> FindAverageVectorRequest {
        ::std::default::Default::default()
    }

    fn generated_message_descriptor_data() -> ::protobuf::reflect::GeneratedMessageDescriptorData {
        let mut fields = ::std::vec::Vec::with_capacity(0);
        let mut oneofs = ::std::vec::Vec::with_capacity(0);
        ::protobuf::reflect::GeneratedMessageDescriptorData::new_2::<FindAverageVectorRequest>(
            "FindAverageVectorRequest",
            fields,
            oneofs,
        )
    }
}

impl ::protobuf::Message for FindAverageVectorRequest {
    const NAME: &'static str = "FindAverageVectorRequest";

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

    fn new() -> FindAverageVectorRequest {
        FindAverageVectorRequest::new()
    }

    fn clear(&mut self) {
        self.special_fields.clear();
    }

    fn default_instance() -> &'static FindAverageVectorRequest {
        static instance: FindAverageVectorRequest = FindAverageVectorRequest {
            special_fields: ::protobuf::SpecialFields::new(),
        };
        &instance
    }
}

impl ::protobuf::MessageFull for FindAverageVectorRequest {
    fn descriptor() -> ::protobuf::reflect::MessageDescriptor {
        static descriptor: ::protobuf::rt::Lazy<::protobuf::reflect::MessageDescriptor> = ::protobuf::rt::Lazy::new();
        descriptor.get(|| file_descriptor().message_by_package_relative_name("FindAverageVectorRequest").unwrap()).clone()
    }
}

impl ::std::fmt::Display for FindAverageVectorRequest {
    fn fmt(&self, f: &mut ::std::fmt::Formatter<'_>) -> ::std::fmt::Result {
        ::protobuf::text_format::fmt(self, f)
    }
}

impl ::protobuf::reflect::ProtobufValue for FindAverageVectorRequest {
    type RuntimeType = ::protobuf::reflect::rt::RuntimeTypeMessage<Self>;
}

#[derive(PartialEq,Clone,Default,Debug)]
// @@protoc_insertion_point(message:proto.FindAverageVectorResponse)
pub struct FindAverageVectorResponse {
    // message fields
    // @@protoc_insertion_point(field:proto.FindAverageVectorResponse.vector)
    pub vector: ::protobuf::MessageField<Vector>,
    // special fields
    // @@protoc_insertion_point(special_field:proto.FindAverageVectorResponse.special_fields)
    pub special_fields: ::protobuf::SpecialFields,
}

impl<'a> ::std::default::Default for &'a FindAverageVectorResponse {
    fn default() -> &'a FindAverageVectorResponse {
        <FindAverageVectorResponse as ::protobuf::Message>::default_instance()
    }
}

impl FindAverageVectorResponse {
    pub fn new() -> FindAverageVectorResponse {
        ::std::default::Default::default()
    }

    fn generated_message_descriptor_data() -> ::protobuf::reflect::GeneratedMessageDescriptorData {
        let mut fields = ::std::vec::Vec::with_capacity(1);
        let mut oneofs = ::std::vec::Vec::with_capacity(0);
        fields.push(::protobuf::reflect::rt::v2::make_message_field_accessor::<_, Vector>(
            "vector",
            |m: &FindAverageVectorResponse| { &m.vector },
            |m: &mut FindAverageVectorResponse| { &mut m.vector },
        ));
        ::protobuf::reflect::GeneratedMessageDescriptorData::new_2::<FindAverageVectorResponse>(
            "FindAverageVectorResponse",
            fields,
            oneofs,
        )
    }
}

impl ::protobuf::Message for FindAverageVectorResponse {
    const NAME: &'static str = "FindAverageVectorResponse";

    fn is_initialized(&self) -> bool {
        true
    }

    fn merge_from(&mut self, is: &mut ::protobuf::CodedInputStream<'_>) -> ::protobuf::Result<()> {
        while let Some(tag) = is.read_raw_tag_or_eof()? {
            match tag {
                10 => {
                    ::protobuf::rt::read_singular_message_into_field(is, &mut self.vector)?;
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
        if let Some(v) = self.vector.as_ref() {
            let len = v.compute_size();
            my_size += 1 + ::protobuf::rt::compute_raw_varint64_size(len) + len;
        }
        my_size += ::protobuf::rt::unknown_fields_size(self.special_fields.unknown_fields());
        self.special_fields.cached_size().set(my_size as u32);
        my_size
    }

    fn write_to_with_cached_sizes(&self, os: &mut ::protobuf::CodedOutputStream<'_>) -> ::protobuf::Result<()> {
        if let Some(v) = self.vector.as_ref() {
            ::protobuf::rt::write_message_field_with_cached_size(1, v, os)?;
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

    fn new() -> FindAverageVectorResponse {
        FindAverageVectorResponse::new()
    }

    fn clear(&mut self) {
        self.vector.clear();
        self.special_fields.clear();
    }

    fn default_instance() -> &'static FindAverageVectorResponse {
        static instance: FindAverageVectorResponse = FindAverageVectorResponse {
            vector: ::protobuf::MessageField::none(),
            special_fields: ::protobuf::SpecialFields::new(),
        };
        &instance
    }
}

impl ::protobuf::MessageFull for FindAverageVectorResponse {
    fn descriptor() -> ::protobuf::reflect::MessageDescriptor {
        static descriptor: ::protobuf::rt::Lazy<::protobuf::reflect::MessageDescriptor> = ::protobuf::rt::Lazy::new();
        descriptor.get(|| file_descriptor().message_by_package_relative_name("FindAverageVectorResponse").unwrap()).clone()
    }
}

impl ::std::fmt::Display for FindAverageVectorResponse {
    fn fmt(&self, f: &mut ::std::fmt::Formatter<'_>) -> ::std::fmt::Result {
        ::protobuf::text_format::fmt(self, f)
    }
}

impl ::protobuf::reflect::ProtobufValue for FindAverageVectorResponse {
    type RuntimeType = ::protobuf::reflect::rt::RuntimeTypeMessage<Self>;
}

static file_descriptor_proto_data: &'static [u8] = b"\
    \n\x16backend_services.proto\x12\x05proto\x1a\x0ccommon.proto\"\x1e\n\
    \x06Vector\x12\x14\n\x05entry\x18\x01\x20\x03(\x02R\x05entry\"R\n\x19Get\
    ClosestNeighborRequest\x12*\n\x06vector\x18\x01\x20\x01(\x0b2\r.proto.Ve\
    ctorH\0R\x06vector\x88\x01\x01B\t\n\x07_vector\"D\n\x1aGetClosestNeighbo\
    rResponse\x12\x1b\n\x06author\x18\x01\x20\x01(\tH\0R\x06author\x88\x01\
    \x01B\t\n\x07_author\"\x1a\n\x18FindAverageVectorRequest\"R\n\x19FindAve\
    rageVectorResponse\x12*\n\x06vector\x18\x01\x20\x01(\x0b2\r.proto.Vector\
    H\0R\x06vector\x88\x01\x01B\t\n\x07_vector2\x86\x02\n\x17SimilarityEngin\
    eService\x12Y\n\x12GetClosestNeighbor\x12\x20.proto.GetClosestNeighborRe\
    quest\x1a!.proto.GetClosestNeighborResponse\x12V\n\x11FindAverageVector\
    \x12\x1f.proto.FindAverageVectorRequest\x1a\x20.proto.FindAverageVectorR\
    esponse\x128\n\x0bCheckHealth\x12\x19.proto.HealthCheckRequest\x1a\x0e.p\
    roto.PayloadB\x18Z\x16app/generated/go/protoJ\x86\x05\n\x06\x12\x04\0\0\
    \x1e\x01\n\x08\n\x01\x0c\x12\x03\0\0\x12\n\x08\n\x01\x02\x12\x03\x02\0\
    \x0e\n\t\n\x02\x03\0\x12\x03\x04\0\x16\n\x08\n\x01\x08\x12\x03\x06\0-\n\
    \t\n\x02\x08\x0b\x12\x03\x06\0-\n\n\n\x02\x04\0\x12\x04\x08\0\n\x01\n\n\
    \n\x03\x04\0\x01\x12\x03\x08\x08\x0e\n\x0b\n\x04\x04\0\x02\0\x12\x03\t\
    \x02\x1b\n\x0c\n\x05\x04\0\x02\0\x04\x12\x03\t\x02\n\n\x0c\n\x05\x04\0\
    \x02\0\x05\x12\x03\t\x0b\x10\n\x0c\n\x05\x04\0\x02\0\x01\x12\x03\t\x11\
    \x16\n\x0c\n\x05\x04\0\x02\0\x03\x12\x03\t\x19\x1a\n\n\n\x02\x04\x01\x12\
    \x04\x0c\0\x0e\x01\n\n\n\x03\x04\x01\x01\x12\x03\x0c\x08!\n\x0b\n\x04\
    \x04\x01\x02\0\x12\x03\r\x02\x1d\n\x0c\n\x05\x04\x01\x02\0\x04\x12\x03\r\
    \x02\n\n\x0c\n\x05\x04\x01\x02\0\x06\x12\x03\r\x0b\x11\n\x0c\n\x05\x04\
    \x01\x02\0\x01\x12\x03\r\x12\x18\n\x0c\n\x05\x04\x01\x02\0\x03\x12\x03\r\
    \x1b\x1c\n\n\n\x02\x04\x02\x12\x04\x0f\0\x11\x01\n\n\n\x03\x04\x02\x01\
    \x12\x03\x0f\x08\"\n\x0b\n\x04\x04\x02\x02\0\x12\x03\x10\x02\x1d\n\x0c\n\
    \x05\x04\x02\x02\0\x04\x12\x03\x10\x02\n\n\x0c\n\x05\x04\x02\x02\0\x05\
    \x12\x03\x10\x0b\x11\n\x0c\n\x05\x04\x02\x02\0\x01\x12\x03\x10\x12\x18\n\
    \x0c\n\x05\x04\x02\x02\0\x03\x12\x03\x10\x1b\x1c\n\t\n\x02\x04\x03\x12\
    \x03\x13\0#\n\n\n\x03\x04\x03\x01\x12\x03\x13\x08\x20\n\n\n\x02\x04\x04\
    \x12\x04\x14\0\x16\x01\n\n\n\x03\x04\x04\x01\x12\x03\x14\x08!\n\x0b\n\
    \x04\x04\x04\x02\0\x12\x03\x15\x02\x1d\n\x0c\n\x05\x04\x04\x02\0\x04\x12\
    \x03\x15\x02\n\n\x0c\n\x05\x04\x04\x02\0\x06\x12\x03\x15\x0b\x11\n\x0c\n\
    \x05\x04\x04\x02\0\x01\x12\x03\x15\x12\x18\n\x0c\n\x05\x04\x04\x02\0\x03\
    \x12\x03\x15\x1b\x1c\n\n\n\x02\x06\0\x12\x04\x18\0\x1e\x01\n\n\n\x03\x06\
    \0\x01\x12\x03\x18\x08\x1f\n\x0c\n\x04\x06\0\x02\0\x12\x04\x19\x02\x1a+\
    \n\x0c\n\x05\x06\0\x02\0\x01\x12\x03\x19\x06\x18\n\x0c\n\x05\x06\0\x02\0\
    \x02\x12\x03\x19\x192\n\x0c\n\x05\x06\0\x02\0\x03\x12\x03\x1a\x0f)\n\x0c\
    \n\x04\x06\0\x02\x01\x12\x04\x1b\x02\x1c*\n\x0c\n\x05\x06\0\x02\x01\x01\
    \x12\x03\x1b\x06\x17\n\x0c\n\x05\x06\0\x02\x01\x02\x12\x03\x1b\x180\n\
    \x0c\n\x05\x06\0\x02\x01\x03\x12\x03\x1c\x0f(\n\x0b\n\x04\x06\0\x02\x02\
    \x12\x03\x1d\x028\n\x0c\n\x05\x06\0\x02\x02\x01\x12\x03\x1d\x06\x11\n\
    \x0c\n\x05\x06\0\x02\x02\x02\x12\x03\x1d\x12$\n\x0c\n\x05\x06\0\x02\x02\
    \x03\x12\x03\x1d/6b\x06proto3\
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
            let mut deps = ::std::vec::Vec::with_capacity(1);
            deps.push(super::common::file_descriptor().clone());
            let mut messages = ::std::vec::Vec::with_capacity(5);
            messages.push(Vector::generated_message_descriptor_data());
            messages.push(GetClosestNeighborRequest::generated_message_descriptor_data());
            messages.push(GetClosestNeighborResponse::generated_message_descriptor_data());
            messages.push(FindAverageVectorRequest::generated_message_descriptor_data());
            messages.push(FindAverageVectorResponse::generated_message_descriptor_data());
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