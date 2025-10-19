import 'package:dartz/dartz.dart';
import 'package:trustify_app/core/error/failure.dart';

abstract interface class VerificationRepository {
  Future<Either<Failure, Map<String, dynamic>>> verifyLink(String url);
  Future<Either<Failure, Map<String, dynamic>>> verifyImage();
}
