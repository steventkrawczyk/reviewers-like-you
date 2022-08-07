// Code generated by protoc-gen-go. DO NOT EDIT.
// versions:
// 	protoc-gen-go v1.28.1
// 	protoc        v3.21.4
// source: resource_services.proto

package proto

import (
	protoreflect "google.golang.org/protobuf/reflect/protoreflect"
	protoimpl "google.golang.org/protobuf/runtime/protoimpl"
	reflect "reflect"
	sync "sync"
)

const (
	// Verify that this generated code is sufficiently up-to-date.
	_ = protoimpl.EnforceVersion(20 - protoimpl.MinVersion)
	// Verify that runtime/protoimpl is sufficiently up-to-date.
	_ = protoimpl.EnforceVersion(protoimpl.MaxVersion - 20)
)

type Action int32

const (
	Action_CREATE Action = 0
	Action_DELETE Action = 1
)

// Enum value maps for Action.
var (
	Action_name = map[int32]string{
		0: "CREATE",
		1: "DELETE",
	}
	Action_value = map[string]int32{
		"CREATE": 0,
		"DELETE": 1,
	}
)

func (x Action) Enum() *Action {
	p := new(Action)
	*p = x
	return p
}

func (x Action) String() string {
	return protoimpl.X.EnumStringOf(x.Descriptor(), protoreflect.EnumNumber(x))
}

func (Action) Descriptor() protoreflect.EnumDescriptor {
	return file_resource_services_proto_enumTypes[0].Descriptor()
}

func (Action) Type() protoreflect.EnumType {
	return &file_resource_services_proto_enumTypes[0]
}

func (x Action) Number() protoreflect.EnumNumber {
	return protoreflect.EnumNumber(x)
}

// Deprecated: Use Action.Descriptor instead.
func (Action) EnumDescriptor() ([]byte, []int) {
	return file_resource_services_proto_rawDescGZIP(), []int{0}
}

type Resource int32

const (
	Resource_TABLE  Resource = 0
	Resource_BUCKET Resource = 1
)

// Enum value maps for Resource.
var (
	Resource_name = map[int32]string{
		0: "TABLE",
		1: "BUCKET",
	}
	Resource_value = map[string]int32{
		"TABLE":  0,
		"BUCKET": 1,
	}
)

func (x Resource) Enum() *Resource {
	p := new(Resource)
	*p = x
	return p
}

func (x Resource) String() string {
	return protoimpl.X.EnumStringOf(x.Descriptor(), protoreflect.EnumNumber(x))
}

func (Resource) Descriptor() protoreflect.EnumDescriptor {
	return file_resource_services_proto_enumTypes[1].Descriptor()
}

func (Resource) Type() protoreflect.EnumType {
	return &file_resource_services_proto_enumTypes[1]
}

func (x Resource) Number() protoreflect.EnumNumber {
	return protoreflect.EnumNumber(x)
}

// Deprecated: Use Resource.Descriptor instead.
func (Resource) EnumDescriptor() ([]byte, []int) {
	return file_resource_services_proto_rawDescGZIP(), []int{1}
}

type UploadReviewRequest struct {
	state         protoimpl.MessageState
	sizeCache     protoimpl.SizeCache
	unknownFields protoimpl.UnknownFields

	Review *Review `protobuf:"bytes,1,opt,name=review,proto3,oneof" json:"review,omitempty"`
}

func (x *UploadReviewRequest) Reset() {
	*x = UploadReviewRequest{}
	if protoimpl.UnsafeEnabled {
		mi := &file_resource_services_proto_msgTypes[0]
		ms := protoimpl.X.MessageStateOf(protoimpl.Pointer(x))
		ms.StoreMessageInfo(mi)
	}
}

func (x *UploadReviewRequest) String() string {
	return protoimpl.X.MessageStringOf(x)
}

func (*UploadReviewRequest) ProtoMessage() {}

func (x *UploadReviewRequest) ProtoReflect() protoreflect.Message {
	mi := &file_resource_services_proto_msgTypes[0]
	if protoimpl.UnsafeEnabled && x != nil {
		ms := protoimpl.X.MessageStateOf(protoimpl.Pointer(x))
		if ms.LoadMessageInfo() == nil {
			ms.StoreMessageInfo(mi)
		}
		return ms
	}
	return mi.MessageOf(x)
}

// Deprecated: Use UploadReviewRequest.ProtoReflect.Descriptor instead.
func (*UploadReviewRequest) Descriptor() ([]byte, []int) {
	return file_resource_services_proto_rawDescGZIP(), []int{0}
}

func (x *UploadReviewRequest) GetReview() *Review {
	if x != nil {
		return x.Review
	}
	return nil
}

type BatchUploadReviewRequest struct {
	state         protoimpl.MessageState
	sizeCache     protoimpl.SizeCache
	unknownFields protoimpl.UnknownFields

	ReviewList *ReviewList `protobuf:"bytes,1,opt,name=reviewList,proto3,oneof" json:"reviewList,omitempty"`
}

func (x *BatchUploadReviewRequest) Reset() {
	*x = BatchUploadReviewRequest{}
	if protoimpl.UnsafeEnabled {
		mi := &file_resource_services_proto_msgTypes[1]
		ms := protoimpl.X.MessageStateOf(protoimpl.Pointer(x))
		ms.StoreMessageInfo(mi)
	}
}

func (x *BatchUploadReviewRequest) String() string {
	return protoimpl.X.MessageStringOf(x)
}

func (*BatchUploadReviewRequest) ProtoMessage() {}

func (x *BatchUploadReviewRequest) ProtoReflect() protoreflect.Message {
	mi := &file_resource_services_proto_msgTypes[1]
	if protoimpl.UnsafeEnabled && x != nil {
		ms := protoimpl.X.MessageStateOf(protoimpl.Pointer(x))
		if ms.LoadMessageInfo() == nil {
			ms.StoreMessageInfo(mi)
		}
		return ms
	}
	return mi.MessageOf(x)
}

// Deprecated: Use BatchUploadReviewRequest.ProtoReflect.Descriptor instead.
func (*BatchUploadReviewRequest) Descriptor() ([]byte, []int) {
	return file_resource_services_proto_rawDescGZIP(), []int{1}
}

func (x *BatchUploadReviewRequest) GetReviewList() *ReviewList {
	if x != nil {
		return x.ReviewList
	}
	return nil
}

type GetReviewsByAuthorRequest struct {
	state         protoimpl.MessageState
	sizeCache     protoimpl.SizeCache
	unknownFields protoimpl.UnknownFields

	Author *string `protobuf:"bytes,1,opt,name=author,proto3,oneof" json:"author,omitempty"`
}

func (x *GetReviewsByAuthorRequest) Reset() {
	*x = GetReviewsByAuthorRequest{}
	if protoimpl.UnsafeEnabled {
		mi := &file_resource_services_proto_msgTypes[2]
		ms := protoimpl.X.MessageStateOf(protoimpl.Pointer(x))
		ms.StoreMessageInfo(mi)
	}
}

func (x *GetReviewsByAuthorRequest) String() string {
	return protoimpl.X.MessageStringOf(x)
}

func (*GetReviewsByAuthorRequest) ProtoMessage() {}

func (x *GetReviewsByAuthorRequest) ProtoReflect() protoreflect.Message {
	mi := &file_resource_services_proto_msgTypes[2]
	if protoimpl.UnsafeEnabled && x != nil {
		ms := protoimpl.X.MessageStateOf(protoimpl.Pointer(x))
		if ms.LoadMessageInfo() == nil {
			ms.StoreMessageInfo(mi)
		}
		return ms
	}
	return mi.MessageOf(x)
}

// Deprecated: Use GetReviewsByAuthorRequest.ProtoReflect.Descriptor instead.
func (*GetReviewsByAuthorRequest) Descriptor() ([]byte, []int) {
	return file_resource_services_proto_rawDescGZIP(), []int{2}
}

func (x *GetReviewsByAuthorRequest) GetAuthor() string {
	if x != nil && x.Author != nil {
		return *x.Author
	}
	return ""
}

type GetAuthorsRequest struct {
	state         protoimpl.MessageState
	sizeCache     protoimpl.SizeCache
	unknownFields protoimpl.UnknownFields
}

func (x *GetAuthorsRequest) Reset() {
	*x = GetAuthorsRequest{}
	if protoimpl.UnsafeEnabled {
		mi := &file_resource_services_proto_msgTypes[3]
		ms := protoimpl.X.MessageStateOf(protoimpl.Pointer(x))
		ms.StoreMessageInfo(mi)
	}
}

func (x *GetAuthorsRequest) String() string {
	return protoimpl.X.MessageStringOf(x)
}

func (*GetAuthorsRequest) ProtoMessage() {}

func (x *GetAuthorsRequest) ProtoReflect() protoreflect.Message {
	mi := &file_resource_services_proto_msgTypes[3]
	if protoimpl.UnsafeEnabled && x != nil {
		ms := protoimpl.X.MessageStateOf(protoimpl.Pointer(x))
		if ms.LoadMessageInfo() == nil {
			ms.StoreMessageInfo(mi)
		}
		return ms
	}
	return mi.MessageOf(x)
}

// Deprecated: Use GetAuthorsRequest.ProtoReflect.Descriptor instead.
func (*GetAuthorsRequest) Descriptor() ([]byte, []int) {
	return file_resource_services_proto_rawDescGZIP(), []int{3}
}

type GetReviewsByAuthorResponse struct {
	state         protoimpl.MessageState
	sizeCache     protoimpl.SizeCache
	unknownFields protoimpl.UnknownFields

	ReviewList *ReviewList `protobuf:"bytes,1,opt,name=reviewList,proto3,oneof" json:"reviewList,omitempty"`
}

func (x *GetReviewsByAuthorResponse) Reset() {
	*x = GetReviewsByAuthorResponse{}
	if protoimpl.UnsafeEnabled {
		mi := &file_resource_services_proto_msgTypes[4]
		ms := protoimpl.X.MessageStateOf(protoimpl.Pointer(x))
		ms.StoreMessageInfo(mi)
	}
}

func (x *GetReviewsByAuthorResponse) String() string {
	return protoimpl.X.MessageStringOf(x)
}

func (*GetReviewsByAuthorResponse) ProtoMessage() {}

func (x *GetReviewsByAuthorResponse) ProtoReflect() protoreflect.Message {
	mi := &file_resource_services_proto_msgTypes[4]
	if protoimpl.UnsafeEnabled && x != nil {
		ms := protoimpl.X.MessageStateOf(protoimpl.Pointer(x))
		if ms.LoadMessageInfo() == nil {
			ms.StoreMessageInfo(mi)
		}
		return ms
	}
	return mi.MessageOf(x)
}

// Deprecated: Use GetReviewsByAuthorResponse.ProtoReflect.Descriptor instead.
func (*GetReviewsByAuthorResponse) Descriptor() ([]byte, []int) {
	return file_resource_services_proto_rawDescGZIP(), []int{4}
}

func (x *GetReviewsByAuthorResponse) GetReviewList() *ReviewList {
	if x != nil {
		return x.ReviewList
	}
	return nil
}

type GetAuthorsResponse struct {
	state         protoimpl.MessageState
	sizeCache     protoimpl.SizeCache
	unknownFields protoimpl.UnknownFields

	Author []string `protobuf:"bytes,1,rep,name=author,proto3" json:"author,omitempty"`
}

func (x *GetAuthorsResponse) Reset() {
	*x = GetAuthorsResponse{}
	if protoimpl.UnsafeEnabled {
		mi := &file_resource_services_proto_msgTypes[5]
		ms := protoimpl.X.MessageStateOf(protoimpl.Pointer(x))
		ms.StoreMessageInfo(mi)
	}
}

func (x *GetAuthorsResponse) String() string {
	return protoimpl.X.MessageStringOf(x)
}

func (*GetAuthorsResponse) ProtoMessage() {}

func (x *GetAuthorsResponse) ProtoReflect() protoreflect.Message {
	mi := &file_resource_services_proto_msgTypes[5]
	if protoimpl.UnsafeEnabled && x != nil {
		ms := protoimpl.X.MessageStateOf(protoimpl.Pointer(x))
		if ms.LoadMessageInfo() == nil {
			ms.StoreMessageInfo(mi)
		}
		return ms
	}
	return mi.MessageOf(x)
}

// Deprecated: Use GetAuthorsResponse.ProtoReflect.Descriptor instead.
func (*GetAuthorsResponse) Descriptor() ([]byte, []int) {
	return file_resource_services_proto_rawDescGZIP(), []int{5}
}

func (x *GetAuthorsResponse) GetAuthor() []string {
	if x != nil {
		return x.Author
	}
	return nil
}

type UploadObjectRequest struct {
	state         protoimpl.MessageState
	sizeCache     protoimpl.SizeCache
	unknownFields protoimpl.UnknownFields

	BucketName       *string `protobuf:"bytes,1,opt,name=bucketName,proto3,oneof" json:"bucketName,omitempty"`
	ObjectName       *string `protobuf:"bytes,2,opt,name=objectName,proto3,oneof" json:"objectName,omitempty"`
	SerializedObject *string `protobuf:"bytes,3,opt,name=serializedObject,proto3,oneof" json:"serializedObject,omitempty"`
}

func (x *UploadObjectRequest) Reset() {
	*x = UploadObjectRequest{}
	if protoimpl.UnsafeEnabled {
		mi := &file_resource_services_proto_msgTypes[6]
		ms := protoimpl.X.MessageStateOf(protoimpl.Pointer(x))
		ms.StoreMessageInfo(mi)
	}
}

func (x *UploadObjectRequest) String() string {
	return protoimpl.X.MessageStringOf(x)
}

func (*UploadObjectRequest) ProtoMessage() {}

func (x *UploadObjectRequest) ProtoReflect() protoreflect.Message {
	mi := &file_resource_services_proto_msgTypes[6]
	if protoimpl.UnsafeEnabled && x != nil {
		ms := protoimpl.X.MessageStateOf(protoimpl.Pointer(x))
		if ms.LoadMessageInfo() == nil {
			ms.StoreMessageInfo(mi)
		}
		return ms
	}
	return mi.MessageOf(x)
}

// Deprecated: Use UploadObjectRequest.ProtoReflect.Descriptor instead.
func (*UploadObjectRequest) Descriptor() ([]byte, []int) {
	return file_resource_services_proto_rawDescGZIP(), []int{6}
}

func (x *UploadObjectRequest) GetBucketName() string {
	if x != nil && x.BucketName != nil {
		return *x.BucketName
	}
	return ""
}

func (x *UploadObjectRequest) GetObjectName() string {
	if x != nil && x.ObjectName != nil {
		return *x.ObjectName
	}
	return ""
}

func (x *UploadObjectRequest) GetSerializedObject() string {
	if x != nil && x.SerializedObject != nil {
		return *x.SerializedObject
	}
	return ""
}

type DownloadObjectRequest struct {
	state         protoimpl.MessageState
	sizeCache     protoimpl.SizeCache
	unknownFields protoimpl.UnknownFields

	BucketName *string `protobuf:"bytes,1,opt,name=bucketName,proto3,oneof" json:"bucketName,omitempty"`
	ObjectName *string `protobuf:"bytes,2,opt,name=objectName,proto3,oneof" json:"objectName,omitempty"`
}

func (x *DownloadObjectRequest) Reset() {
	*x = DownloadObjectRequest{}
	if protoimpl.UnsafeEnabled {
		mi := &file_resource_services_proto_msgTypes[7]
		ms := protoimpl.X.MessageStateOf(protoimpl.Pointer(x))
		ms.StoreMessageInfo(mi)
	}
}

func (x *DownloadObjectRequest) String() string {
	return protoimpl.X.MessageStringOf(x)
}

func (*DownloadObjectRequest) ProtoMessage() {}

func (x *DownloadObjectRequest) ProtoReflect() protoreflect.Message {
	mi := &file_resource_services_proto_msgTypes[7]
	if protoimpl.UnsafeEnabled && x != nil {
		ms := protoimpl.X.MessageStateOf(protoimpl.Pointer(x))
		if ms.LoadMessageInfo() == nil {
			ms.StoreMessageInfo(mi)
		}
		return ms
	}
	return mi.MessageOf(x)
}

// Deprecated: Use DownloadObjectRequest.ProtoReflect.Descriptor instead.
func (*DownloadObjectRequest) Descriptor() ([]byte, []int) {
	return file_resource_services_proto_rawDescGZIP(), []int{7}
}

func (x *DownloadObjectRequest) GetBucketName() string {
	if x != nil && x.BucketName != nil {
		return *x.BucketName
	}
	return ""
}

func (x *DownloadObjectRequest) GetObjectName() string {
	if x != nil && x.ObjectName != nil {
		return *x.ObjectName
	}
	return ""
}

type ManageResourceRequest struct {
	state         protoimpl.MessageState
	sizeCache     protoimpl.SizeCache
	unknownFields protoimpl.UnknownFields

	Name     *string   `protobuf:"bytes,1,opt,name=name,proto3,oneof" json:"name,omitempty"`
	Action   *Action   `protobuf:"varint,2,opt,name=action,proto3,enum=proto.Action,oneof" json:"action,omitempty"`
	Resource *Resource `protobuf:"varint,3,opt,name=resource,proto3,enum=proto.Resource,oneof" json:"resource,omitempty"`
}

func (x *ManageResourceRequest) Reset() {
	*x = ManageResourceRequest{}
	if protoimpl.UnsafeEnabled {
		mi := &file_resource_services_proto_msgTypes[8]
		ms := protoimpl.X.MessageStateOf(protoimpl.Pointer(x))
		ms.StoreMessageInfo(mi)
	}
}

func (x *ManageResourceRequest) String() string {
	return protoimpl.X.MessageStringOf(x)
}

func (*ManageResourceRequest) ProtoMessage() {}

func (x *ManageResourceRequest) ProtoReflect() protoreflect.Message {
	mi := &file_resource_services_proto_msgTypes[8]
	if protoimpl.UnsafeEnabled && x != nil {
		ms := protoimpl.X.MessageStateOf(protoimpl.Pointer(x))
		if ms.LoadMessageInfo() == nil {
			ms.StoreMessageInfo(mi)
		}
		return ms
	}
	return mi.MessageOf(x)
}

// Deprecated: Use ManageResourceRequest.ProtoReflect.Descriptor instead.
func (*ManageResourceRequest) Descriptor() ([]byte, []int) {
	return file_resource_services_proto_rawDescGZIP(), []int{8}
}

func (x *ManageResourceRequest) GetName() string {
	if x != nil && x.Name != nil {
		return *x.Name
	}
	return ""
}

func (x *ManageResourceRequest) GetAction() Action {
	if x != nil && x.Action != nil {
		return *x.Action
	}
	return Action_CREATE
}

func (x *ManageResourceRequest) GetResource() Resource {
	if x != nil && x.Resource != nil {
		return *x.Resource
	}
	return Resource_TABLE
}

var File_resource_services_proto protoreflect.FileDescriptor

var file_resource_services_proto_rawDesc = []byte{
	0x0a, 0x17, 0x72, 0x65, 0x73, 0x6f, 0x75, 0x72, 0x63, 0x65, 0x5f, 0x73, 0x65, 0x72, 0x76, 0x69,
	0x63, 0x65, 0x73, 0x2e, 0x70, 0x72, 0x6f, 0x74, 0x6f, 0x12, 0x05, 0x70, 0x72, 0x6f, 0x74, 0x6f,
	0x1a, 0x16, 0x61, 0x70, 0x70, 0x2f, 0x70, 0x72, 0x6f, 0x74, 0x6f, 0x2f, 0x63, 0x6f, 0x6d, 0x6d,
	0x6f, 0x6e, 0x2e, 0x70, 0x72, 0x6f, 0x74, 0x6f, 0x1a, 0x1a, 0x61, 0x70, 0x70, 0x2f, 0x70, 0x72,
	0x6f, 0x74, 0x6f, 0x2f, 0x64, 0x61, 0x74, 0x61, 0x5f, 0x6d, 0x6f, 0x64, 0x65, 0x6c, 0x2e, 0x70,
	0x72, 0x6f, 0x74, 0x6f, 0x22, 0x4c, 0x0a, 0x13, 0x55, 0x70, 0x6c, 0x6f, 0x61, 0x64, 0x52, 0x65,
	0x76, 0x69, 0x65, 0x77, 0x52, 0x65, 0x71, 0x75, 0x65, 0x73, 0x74, 0x12, 0x2a, 0x0a, 0x06, 0x72,
	0x65, 0x76, 0x69, 0x65, 0x77, 0x18, 0x01, 0x20, 0x01, 0x28, 0x0b, 0x32, 0x0d, 0x2e, 0x70, 0x72,
	0x6f, 0x74, 0x6f, 0x2e, 0x52, 0x65, 0x76, 0x69, 0x65, 0x77, 0x48, 0x00, 0x52, 0x06, 0x72, 0x65,
	0x76, 0x69, 0x65, 0x77, 0x88, 0x01, 0x01, 0x42, 0x09, 0x0a, 0x07, 0x5f, 0x72, 0x65, 0x76, 0x69,
	0x65, 0x77, 0x22, 0x61, 0x0a, 0x18, 0x42, 0x61, 0x74, 0x63, 0x68, 0x55, 0x70, 0x6c, 0x6f, 0x61,
	0x64, 0x52, 0x65, 0x76, 0x69, 0x65, 0x77, 0x52, 0x65, 0x71, 0x75, 0x65, 0x73, 0x74, 0x12, 0x36,
	0x0a, 0x0a, 0x72, 0x65, 0x76, 0x69, 0x65, 0x77, 0x4c, 0x69, 0x73, 0x74, 0x18, 0x01, 0x20, 0x01,
	0x28, 0x0b, 0x32, 0x11, 0x2e, 0x70, 0x72, 0x6f, 0x74, 0x6f, 0x2e, 0x52, 0x65, 0x76, 0x69, 0x65,
	0x77, 0x4c, 0x69, 0x73, 0x74, 0x48, 0x00, 0x52, 0x0a, 0x72, 0x65, 0x76, 0x69, 0x65, 0x77, 0x4c,
	0x69, 0x73, 0x74, 0x88, 0x01, 0x01, 0x42, 0x0d, 0x0a, 0x0b, 0x5f, 0x72, 0x65, 0x76, 0x69, 0x65,
	0x77, 0x4c, 0x69, 0x73, 0x74, 0x22, 0x43, 0x0a, 0x19, 0x47, 0x65, 0x74, 0x52, 0x65, 0x76, 0x69,
	0x65, 0x77, 0x73, 0x42, 0x79, 0x41, 0x75, 0x74, 0x68, 0x6f, 0x72, 0x52, 0x65, 0x71, 0x75, 0x65,
	0x73, 0x74, 0x12, 0x1b, 0x0a, 0x06, 0x61, 0x75, 0x74, 0x68, 0x6f, 0x72, 0x18, 0x01, 0x20, 0x01,
	0x28, 0x09, 0x48, 0x00, 0x52, 0x06, 0x61, 0x75, 0x74, 0x68, 0x6f, 0x72, 0x88, 0x01, 0x01, 0x42,
	0x09, 0x0a, 0x07, 0x5f, 0x61, 0x75, 0x74, 0x68, 0x6f, 0x72, 0x22, 0x13, 0x0a, 0x11, 0x47, 0x65,
	0x74, 0x41, 0x75, 0x74, 0x68, 0x6f, 0x72, 0x73, 0x52, 0x65, 0x71, 0x75, 0x65, 0x73, 0x74, 0x22,
	0x63, 0x0a, 0x1a, 0x47, 0x65, 0x74, 0x52, 0x65, 0x76, 0x69, 0x65, 0x77, 0x73, 0x42, 0x79, 0x41,
	0x75, 0x74, 0x68, 0x6f, 0x72, 0x52, 0x65, 0x73, 0x70, 0x6f, 0x6e, 0x73, 0x65, 0x12, 0x36, 0x0a,
	0x0a, 0x72, 0x65, 0x76, 0x69, 0x65, 0x77, 0x4c, 0x69, 0x73, 0x74, 0x18, 0x01, 0x20, 0x01, 0x28,
	0x0b, 0x32, 0x11, 0x2e, 0x70, 0x72, 0x6f, 0x74, 0x6f, 0x2e, 0x52, 0x65, 0x76, 0x69, 0x65, 0x77,
	0x4c, 0x69, 0x73, 0x74, 0x48, 0x00, 0x52, 0x0a, 0x72, 0x65, 0x76, 0x69, 0x65, 0x77, 0x4c, 0x69,
	0x73, 0x74, 0x88, 0x01, 0x01, 0x42, 0x0d, 0x0a, 0x0b, 0x5f, 0x72, 0x65, 0x76, 0x69, 0x65, 0x77,
	0x4c, 0x69, 0x73, 0x74, 0x22, 0x2c, 0x0a, 0x12, 0x47, 0x65, 0x74, 0x41, 0x75, 0x74, 0x68, 0x6f,
	0x72, 0x73, 0x52, 0x65, 0x73, 0x70, 0x6f, 0x6e, 0x73, 0x65, 0x12, 0x16, 0x0a, 0x06, 0x61, 0x75,
	0x74, 0x68, 0x6f, 0x72, 0x18, 0x01, 0x20, 0x03, 0x28, 0x09, 0x52, 0x06, 0x61, 0x75, 0x74, 0x68,
	0x6f, 0x72, 0x22, 0xc3, 0x01, 0x0a, 0x13, 0x55, 0x70, 0x6c, 0x6f, 0x61, 0x64, 0x4f, 0x62, 0x6a,
	0x65, 0x63, 0x74, 0x52, 0x65, 0x71, 0x75, 0x65, 0x73, 0x74, 0x12, 0x23, 0x0a, 0x0a, 0x62, 0x75,
	0x63, 0x6b, 0x65, 0x74, 0x4e, 0x61, 0x6d, 0x65, 0x18, 0x01, 0x20, 0x01, 0x28, 0x09, 0x48, 0x00,
	0x52, 0x0a, 0x62, 0x75, 0x63, 0x6b, 0x65, 0x74, 0x4e, 0x61, 0x6d, 0x65, 0x88, 0x01, 0x01, 0x12,
	0x23, 0x0a, 0x0a, 0x6f, 0x62, 0x6a, 0x65, 0x63, 0x74, 0x4e, 0x61, 0x6d, 0x65, 0x18, 0x02, 0x20,
	0x01, 0x28, 0x09, 0x48, 0x01, 0x52, 0x0a, 0x6f, 0x62, 0x6a, 0x65, 0x63, 0x74, 0x4e, 0x61, 0x6d,
	0x65, 0x88, 0x01, 0x01, 0x12, 0x2f, 0x0a, 0x10, 0x73, 0x65, 0x72, 0x69, 0x61, 0x6c, 0x69, 0x7a,
	0x65, 0x64, 0x4f, 0x62, 0x6a, 0x65, 0x63, 0x74, 0x18, 0x03, 0x20, 0x01, 0x28, 0x09, 0x48, 0x02,
	0x52, 0x10, 0x73, 0x65, 0x72, 0x69, 0x61, 0x6c, 0x69, 0x7a, 0x65, 0x64, 0x4f, 0x62, 0x6a, 0x65,
	0x63, 0x74, 0x88, 0x01, 0x01, 0x42, 0x0d, 0x0a, 0x0b, 0x5f, 0x62, 0x75, 0x63, 0x6b, 0x65, 0x74,
	0x4e, 0x61, 0x6d, 0x65, 0x42, 0x0d, 0x0a, 0x0b, 0x5f, 0x6f, 0x62, 0x6a, 0x65, 0x63, 0x74, 0x4e,
	0x61, 0x6d, 0x65, 0x42, 0x13, 0x0a, 0x11, 0x5f, 0x73, 0x65, 0x72, 0x69, 0x61, 0x6c, 0x69, 0x7a,
	0x65, 0x64, 0x4f, 0x62, 0x6a, 0x65, 0x63, 0x74, 0x22, 0x7f, 0x0a, 0x15, 0x44, 0x6f, 0x77, 0x6e,
	0x6c, 0x6f, 0x61, 0x64, 0x4f, 0x62, 0x6a, 0x65, 0x63, 0x74, 0x52, 0x65, 0x71, 0x75, 0x65, 0x73,
	0x74, 0x12, 0x23, 0x0a, 0x0a, 0x62, 0x75, 0x63, 0x6b, 0x65, 0x74, 0x4e, 0x61, 0x6d, 0x65, 0x18,
	0x01, 0x20, 0x01, 0x28, 0x09, 0x48, 0x00, 0x52, 0x0a, 0x62, 0x75, 0x63, 0x6b, 0x65, 0x74, 0x4e,
	0x61, 0x6d, 0x65, 0x88, 0x01, 0x01, 0x12, 0x23, 0x0a, 0x0a, 0x6f, 0x62, 0x6a, 0x65, 0x63, 0x74,
	0x4e, 0x61, 0x6d, 0x65, 0x18, 0x02, 0x20, 0x01, 0x28, 0x09, 0x48, 0x01, 0x52, 0x0a, 0x6f, 0x62,
	0x6a, 0x65, 0x63, 0x74, 0x4e, 0x61, 0x6d, 0x65, 0x88, 0x01, 0x01, 0x42, 0x0d, 0x0a, 0x0b, 0x5f,
	0x62, 0x75, 0x63, 0x6b, 0x65, 0x74, 0x4e, 0x61, 0x6d, 0x65, 0x42, 0x0d, 0x0a, 0x0b, 0x5f, 0x6f,
	0x62, 0x6a, 0x65, 0x63, 0x74, 0x4e, 0x61, 0x6d, 0x65, 0x22, 0xaf, 0x01, 0x0a, 0x15, 0x4d, 0x61,
	0x6e, 0x61, 0x67, 0x65, 0x52, 0x65, 0x73, 0x6f, 0x75, 0x72, 0x63, 0x65, 0x52, 0x65, 0x71, 0x75,
	0x65, 0x73, 0x74, 0x12, 0x17, 0x0a, 0x04, 0x6e, 0x61, 0x6d, 0x65, 0x18, 0x01, 0x20, 0x01, 0x28,
	0x09, 0x48, 0x00, 0x52, 0x04, 0x6e, 0x61, 0x6d, 0x65, 0x88, 0x01, 0x01, 0x12, 0x2a, 0x0a, 0x06,
	0x61, 0x63, 0x74, 0x69, 0x6f, 0x6e, 0x18, 0x02, 0x20, 0x01, 0x28, 0x0e, 0x32, 0x0d, 0x2e, 0x70,
	0x72, 0x6f, 0x74, 0x6f, 0x2e, 0x41, 0x63, 0x74, 0x69, 0x6f, 0x6e, 0x48, 0x01, 0x52, 0x06, 0x61,
	0x63, 0x74, 0x69, 0x6f, 0x6e, 0x88, 0x01, 0x01, 0x12, 0x30, 0x0a, 0x08, 0x72, 0x65, 0x73, 0x6f,
	0x75, 0x72, 0x63, 0x65, 0x18, 0x03, 0x20, 0x01, 0x28, 0x0e, 0x32, 0x0f, 0x2e, 0x70, 0x72, 0x6f,
	0x74, 0x6f, 0x2e, 0x52, 0x65, 0x73, 0x6f, 0x75, 0x72, 0x63, 0x65, 0x48, 0x02, 0x52, 0x08, 0x72,
	0x65, 0x73, 0x6f, 0x75, 0x72, 0x63, 0x65, 0x88, 0x01, 0x01, 0x42, 0x07, 0x0a, 0x05, 0x5f, 0x6e,
	0x61, 0x6d, 0x65, 0x42, 0x09, 0x0a, 0x07, 0x5f, 0x61, 0x63, 0x74, 0x69, 0x6f, 0x6e, 0x42, 0x0b,
	0x0a, 0x09, 0x5f, 0x72, 0x65, 0x73, 0x6f, 0x75, 0x72, 0x63, 0x65, 0x2a, 0x20, 0x0a, 0x06, 0x41,
	0x63, 0x74, 0x69, 0x6f, 0x6e, 0x12, 0x0a, 0x0a, 0x06, 0x43, 0x52, 0x45, 0x41, 0x54, 0x45, 0x10,
	0x00, 0x12, 0x0a, 0x0a, 0x06, 0x44, 0x45, 0x4c, 0x45, 0x54, 0x45, 0x10, 0x01, 0x2a, 0x21, 0x0a,
	0x08, 0x52, 0x65, 0x73, 0x6f, 0x75, 0x72, 0x63, 0x65, 0x12, 0x09, 0x0a, 0x05, 0x54, 0x41, 0x42,
	0x4c, 0x45, 0x10, 0x00, 0x12, 0x0a, 0x0a, 0x06, 0x42, 0x55, 0x43, 0x4b, 0x45, 0x54, 0x10, 0x01,
	0x32, 0xb6, 0x02, 0x0a, 0x14, 0x4d, 0x61, 0x69, 0x6e, 0x44, 0x61, 0x74, 0x61, 0x73, 0x74, 0x6f,
	0x72, 0x65, 0x53, 0x65, 0x72, 0x76, 0x69, 0x63, 0x65, 0x12, 0x3a, 0x0a, 0x0c, 0x55, 0x70, 0x6c,
	0x6f, 0x61, 0x64, 0x52, 0x65, 0x76, 0x69, 0x65, 0x77, 0x12, 0x1a, 0x2e, 0x70, 0x72, 0x6f, 0x74,
	0x6f, 0x2e, 0x55, 0x70, 0x6c, 0x6f, 0x61, 0x64, 0x52, 0x65, 0x76, 0x69, 0x65, 0x77, 0x52, 0x65,
	0x71, 0x75, 0x65, 0x73, 0x74, 0x1a, 0x0e, 0x2e, 0x70, 0x72, 0x6f, 0x74, 0x6f, 0x2e, 0x50, 0x61,
	0x79, 0x6c, 0x6f, 0x61, 0x64, 0x12, 0x44, 0x0a, 0x11, 0x42, 0x61, 0x74, 0x63, 0x68, 0x55, 0x70,
	0x6c, 0x6f, 0x61, 0x64, 0x52, 0x65, 0x76, 0x69, 0x65, 0x77, 0x12, 0x1f, 0x2e, 0x70, 0x72, 0x6f,
	0x74, 0x6f, 0x2e, 0x42, 0x61, 0x74, 0x63, 0x68, 0x55, 0x70, 0x6c, 0x6f, 0x61, 0x64, 0x52, 0x65,
	0x76, 0x69, 0x65, 0x77, 0x52, 0x65, 0x71, 0x75, 0x65, 0x73, 0x74, 0x1a, 0x0e, 0x2e, 0x70, 0x72,
	0x6f, 0x74, 0x6f, 0x2e, 0x50, 0x61, 0x79, 0x6c, 0x6f, 0x61, 0x64, 0x12, 0x59, 0x0a, 0x12, 0x47,
	0x65, 0x74, 0x52, 0x65, 0x76, 0x69, 0x65, 0x77, 0x73, 0x42, 0x79, 0x41, 0x75, 0x74, 0x68, 0x6f,
	0x72, 0x12, 0x20, 0x2e, 0x70, 0x72, 0x6f, 0x74, 0x6f, 0x2e, 0x47, 0x65, 0x74, 0x52, 0x65, 0x76,
	0x69, 0x65, 0x77, 0x73, 0x42, 0x79, 0x41, 0x75, 0x74, 0x68, 0x6f, 0x72, 0x52, 0x65, 0x71, 0x75,
	0x65, 0x73, 0x74, 0x1a, 0x21, 0x2e, 0x70, 0x72, 0x6f, 0x74, 0x6f, 0x2e, 0x47, 0x65, 0x74, 0x52,
	0x65, 0x76, 0x69, 0x65, 0x77, 0x73, 0x42, 0x79, 0x41, 0x75, 0x74, 0x68, 0x6f, 0x72, 0x52, 0x65,
	0x73, 0x70, 0x6f, 0x6e, 0x73, 0x65, 0x12, 0x41, 0x0a, 0x0a, 0x47, 0x65, 0x74, 0x41, 0x75, 0x74,
	0x68, 0x6f, 0x72, 0x73, 0x12, 0x18, 0x2e, 0x70, 0x72, 0x6f, 0x74, 0x6f, 0x2e, 0x47, 0x65, 0x74,
	0x41, 0x75, 0x74, 0x68, 0x6f, 0x72, 0x73, 0x52, 0x65, 0x71, 0x75, 0x65, 0x73, 0x74, 0x1a, 0x19,
	0x2e, 0x70, 0x72, 0x6f, 0x74, 0x6f, 0x2e, 0x47, 0x65, 0x74, 0x41, 0x75, 0x74, 0x68, 0x6f, 0x72,
	0x73, 0x52, 0x65, 0x73, 0x70, 0x6f, 0x6e, 0x73, 0x65, 0x32, 0x8e, 0x01, 0x0a, 0x10, 0x46, 0x69,
	0x6c, 0x65, 0x73, 0x74, 0x6f, 0x72, 0x65, 0x53, 0x65, 0x72, 0x76, 0x69, 0x63, 0x65, 0x12, 0x3a,
	0x0a, 0x0c, 0x55, 0x70, 0x6c, 0x6f, 0x61, 0x64, 0x4f, 0x62, 0x6a, 0x65, 0x63, 0x74, 0x12, 0x1a,
	0x2e, 0x70, 0x72, 0x6f, 0x74, 0x6f, 0x2e, 0x55, 0x70, 0x6c, 0x6f, 0x61, 0x64, 0x4f, 0x62, 0x6a,
	0x65, 0x63, 0x74, 0x52, 0x65, 0x71, 0x75, 0x65, 0x73, 0x74, 0x1a, 0x0e, 0x2e, 0x70, 0x72, 0x6f,
	0x74, 0x6f, 0x2e, 0x50, 0x61, 0x79, 0x6c, 0x6f, 0x61, 0x64, 0x12, 0x3e, 0x0a, 0x0e, 0x44, 0x6f,
	0x77, 0x6e, 0x6c, 0x6f, 0x61, 0x64, 0x4f, 0x62, 0x6a, 0x65, 0x63, 0x74, 0x12, 0x1c, 0x2e, 0x70,
	0x72, 0x6f, 0x74, 0x6f, 0x2e, 0x44, 0x6f, 0x77, 0x6e, 0x6c, 0x6f, 0x61, 0x64, 0x4f, 0x62, 0x6a,
	0x65, 0x63, 0x74, 0x52, 0x65, 0x71, 0x75, 0x65, 0x73, 0x74, 0x1a, 0x0e, 0x2e, 0x70, 0x72, 0x6f,
	0x74, 0x6f, 0x2e, 0x50, 0x61, 0x79, 0x6c, 0x6f, 0x61, 0x64, 0x32, 0x91, 0x01, 0x0a, 0x15, 0x44,
	0x61, 0x74, 0x61, 0x73, 0x74, 0x6f, 0x72, 0x65, 0x41, 0x64, 0x6d, 0x69, 0x6e, 0x53, 0x65, 0x72,
	0x76, 0x69, 0x63, 0x65, 0x12, 0x3e, 0x0a, 0x0e, 0x4d, 0x61, 0x6e, 0x61, 0x67, 0x65, 0x52, 0x65,
	0x73, 0x6f, 0x75, 0x72, 0x63, 0x65, 0x12, 0x1c, 0x2e, 0x70, 0x72, 0x6f, 0x74, 0x6f, 0x2e, 0x4d,
	0x61, 0x6e, 0x61, 0x67, 0x65, 0x52, 0x65, 0x73, 0x6f, 0x75, 0x72, 0x63, 0x65, 0x52, 0x65, 0x71,
	0x75, 0x65, 0x73, 0x74, 0x1a, 0x0e, 0x2e, 0x70, 0x72, 0x6f, 0x74, 0x6f, 0x2e, 0x50, 0x61, 0x79,
	0x6c, 0x6f, 0x61, 0x64, 0x12, 0x38, 0x0a, 0x0b, 0x43, 0x68, 0x65, 0x63, 0x6b, 0x48, 0x65, 0x61,
	0x6c, 0x74, 0x68, 0x12, 0x19, 0x2e, 0x70, 0x72, 0x6f, 0x74, 0x6f, 0x2e, 0x48, 0x65, 0x61, 0x6c,
	0x74, 0x68, 0x43, 0x68, 0x65, 0x63, 0x6b, 0x52, 0x65, 0x71, 0x75, 0x65, 0x73, 0x74, 0x1a, 0x0e,
	0x2e, 0x70, 0x72, 0x6f, 0x74, 0x6f, 0x2e, 0x50, 0x61, 0x79, 0x6c, 0x6f, 0x61, 0x64, 0x42, 0x18,
	0x5a, 0x16, 0x61, 0x70, 0x70, 0x2f, 0x67, 0x65, 0x6e, 0x65, 0x72, 0x61, 0x74, 0x65, 0x64, 0x2f,
	0x67, 0x6f, 0x2f, 0x70, 0x72, 0x6f, 0x74, 0x6f, 0x62, 0x06, 0x70, 0x72, 0x6f, 0x74, 0x6f, 0x33,
}

var (
	file_resource_services_proto_rawDescOnce sync.Once
	file_resource_services_proto_rawDescData = file_resource_services_proto_rawDesc
)

func file_resource_services_proto_rawDescGZIP() []byte {
	file_resource_services_proto_rawDescOnce.Do(func() {
		file_resource_services_proto_rawDescData = protoimpl.X.CompressGZIP(file_resource_services_proto_rawDescData)
	})
	return file_resource_services_proto_rawDescData
}

var file_resource_services_proto_enumTypes = make([]protoimpl.EnumInfo, 2)
var file_resource_services_proto_msgTypes = make([]protoimpl.MessageInfo, 9)
var file_resource_services_proto_goTypes = []interface{}{
	(Action)(0),                        // 0: proto.Action
	(Resource)(0),                      // 1: proto.Resource
	(*UploadReviewRequest)(nil),        // 2: proto.UploadReviewRequest
	(*BatchUploadReviewRequest)(nil),   // 3: proto.BatchUploadReviewRequest
	(*GetReviewsByAuthorRequest)(nil),  // 4: proto.GetReviewsByAuthorRequest
	(*GetAuthorsRequest)(nil),          // 5: proto.GetAuthorsRequest
	(*GetReviewsByAuthorResponse)(nil), // 6: proto.GetReviewsByAuthorResponse
	(*GetAuthorsResponse)(nil),         // 7: proto.GetAuthorsResponse
	(*UploadObjectRequest)(nil),        // 8: proto.UploadObjectRequest
	(*DownloadObjectRequest)(nil),      // 9: proto.DownloadObjectRequest
	(*ManageResourceRequest)(nil),      // 10: proto.ManageResourceRequest
	(*Review)(nil),                     // 11: proto.Review
	(*ReviewList)(nil),                 // 12: proto.ReviewList
	(*HealthCheckRequest)(nil),         // 13: proto.HealthCheckRequest
	(*Payload)(nil),                    // 14: proto.Payload
}
var file_resource_services_proto_depIdxs = []int32{
	11, // 0: proto.UploadReviewRequest.review:type_name -> proto.Review
	12, // 1: proto.BatchUploadReviewRequest.reviewList:type_name -> proto.ReviewList
	12, // 2: proto.GetReviewsByAuthorResponse.reviewList:type_name -> proto.ReviewList
	0,  // 3: proto.ManageResourceRequest.action:type_name -> proto.Action
	1,  // 4: proto.ManageResourceRequest.resource:type_name -> proto.Resource
	2,  // 5: proto.MainDatastoreService.UploadReview:input_type -> proto.UploadReviewRequest
	3,  // 6: proto.MainDatastoreService.BatchUploadReview:input_type -> proto.BatchUploadReviewRequest
	4,  // 7: proto.MainDatastoreService.GetReviewsByAuthor:input_type -> proto.GetReviewsByAuthorRequest
	5,  // 8: proto.MainDatastoreService.GetAuthors:input_type -> proto.GetAuthorsRequest
	8,  // 9: proto.FilestoreService.UploadObject:input_type -> proto.UploadObjectRequest
	9,  // 10: proto.FilestoreService.DownloadObject:input_type -> proto.DownloadObjectRequest
	10, // 11: proto.DatastoreAdminService.ManageResource:input_type -> proto.ManageResourceRequest
	13, // 12: proto.DatastoreAdminService.CheckHealth:input_type -> proto.HealthCheckRequest
	14, // 13: proto.MainDatastoreService.UploadReview:output_type -> proto.Payload
	14, // 14: proto.MainDatastoreService.BatchUploadReview:output_type -> proto.Payload
	6,  // 15: proto.MainDatastoreService.GetReviewsByAuthor:output_type -> proto.GetReviewsByAuthorResponse
	7,  // 16: proto.MainDatastoreService.GetAuthors:output_type -> proto.GetAuthorsResponse
	14, // 17: proto.FilestoreService.UploadObject:output_type -> proto.Payload
	14, // 18: proto.FilestoreService.DownloadObject:output_type -> proto.Payload
	14, // 19: proto.DatastoreAdminService.ManageResource:output_type -> proto.Payload
	14, // 20: proto.DatastoreAdminService.CheckHealth:output_type -> proto.Payload
	13, // [13:21] is the sub-list for method output_type
	5,  // [5:13] is the sub-list for method input_type
	5,  // [5:5] is the sub-list for extension type_name
	5,  // [5:5] is the sub-list for extension extendee
	0,  // [0:5] is the sub-list for field type_name
}

func init() { file_resource_services_proto_init() }
func file_resource_services_proto_init() {
	if File_resource_services_proto != nil {
		return
	}
	file_app_proto_common_proto_init()
	file_app_proto_data_model_proto_init()
	if !protoimpl.UnsafeEnabled {
		file_resource_services_proto_msgTypes[0].Exporter = func(v interface{}, i int) interface{} {
			switch v := v.(*UploadReviewRequest); i {
			case 0:
				return &v.state
			case 1:
				return &v.sizeCache
			case 2:
				return &v.unknownFields
			default:
				return nil
			}
		}
		file_resource_services_proto_msgTypes[1].Exporter = func(v interface{}, i int) interface{} {
			switch v := v.(*BatchUploadReviewRequest); i {
			case 0:
				return &v.state
			case 1:
				return &v.sizeCache
			case 2:
				return &v.unknownFields
			default:
				return nil
			}
		}
		file_resource_services_proto_msgTypes[2].Exporter = func(v interface{}, i int) interface{} {
			switch v := v.(*GetReviewsByAuthorRequest); i {
			case 0:
				return &v.state
			case 1:
				return &v.sizeCache
			case 2:
				return &v.unknownFields
			default:
				return nil
			}
		}
		file_resource_services_proto_msgTypes[3].Exporter = func(v interface{}, i int) interface{} {
			switch v := v.(*GetAuthorsRequest); i {
			case 0:
				return &v.state
			case 1:
				return &v.sizeCache
			case 2:
				return &v.unknownFields
			default:
				return nil
			}
		}
		file_resource_services_proto_msgTypes[4].Exporter = func(v interface{}, i int) interface{} {
			switch v := v.(*GetReviewsByAuthorResponse); i {
			case 0:
				return &v.state
			case 1:
				return &v.sizeCache
			case 2:
				return &v.unknownFields
			default:
				return nil
			}
		}
		file_resource_services_proto_msgTypes[5].Exporter = func(v interface{}, i int) interface{} {
			switch v := v.(*GetAuthorsResponse); i {
			case 0:
				return &v.state
			case 1:
				return &v.sizeCache
			case 2:
				return &v.unknownFields
			default:
				return nil
			}
		}
		file_resource_services_proto_msgTypes[6].Exporter = func(v interface{}, i int) interface{} {
			switch v := v.(*UploadObjectRequest); i {
			case 0:
				return &v.state
			case 1:
				return &v.sizeCache
			case 2:
				return &v.unknownFields
			default:
				return nil
			}
		}
		file_resource_services_proto_msgTypes[7].Exporter = func(v interface{}, i int) interface{} {
			switch v := v.(*DownloadObjectRequest); i {
			case 0:
				return &v.state
			case 1:
				return &v.sizeCache
			case 2:
				return &v.unknownFields
			default:
				return nil
			}
		}
		file_resource_services_proto_msgTypes[8].Exporter = func(v interface{}, i int) interface{} {
			switch v := v.(*ManageResourceRequest); i {
			case 0:
				return &v.state
			case 1:
				return &v.sizeCache
			case 2:
				return &v.unknownFields
			default:
				return nil
			}
		}
	}
	file_resource_services_proto_msgTypes[0].OneofWrappers = []interface{}{}
	file_resource_services_proto_msgTypes[1].OneofWrappers = []interface{}{}
	file_resource_services_proto_msgTypes[2].OneofWrappers = []interface{}{}
	file_resource_services_proto_msgTypes[4].OneofWrappers = []interface{}{}
	file_resource_services_proto_msgTypes[6].OneofWrappers = []interface{}{}
	file_resource_services_proto_msgTypes[7].OneofWrappers = []interface{}{}
	file_resource_services_proto_msgTypes[8].OneofWrappers = []interface{}{}
	type x struct{}
	out := protoimpl.TypeBuilder{
		File: protoimpl.DescBuilder{
			GoPackagePath: reflect.TypeOf(x{}).PkgPath(),
			RawDescriptor: file_resource_services_proto_rawDesc,
			NumEnums:      2,
			NumMessages:   9,
			NumExtensions: 0,
			NumServices:   3,
		},
		GoTypes:           file_resource_services_proto_goTypes,
		DependencyIndexes: file_resource_services_proto_depIdxs,
		EnumInfos:         file_resource_services_proto_enumTypes,
		MessageInfos:      file_resource_services_proto_msgTypes,
	}.Build()
	File_resource_services_proto = out.File
	file_resource_services_proto_rawDesc = nil
	file_resource_services_proto_goTypes = nil
	file_resource_services_proto_depIdxs = nil
}
